require("dotenv").config();
const OpenAI = require("openai-api");
const openai = new OpenAI(process.env.OPENAI_API_KEY);
const { Client, Intents } = require("discord.js");
const client = new Client({
    intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.login(process.env.BOT_TOKEN);

let defaultPrompt = `Luna is. \nMe: hello Luna\nLuna: Hello!\n`;
let prompt = `Luna is. \nMe: hello Luna\nLuna: Hello!\n`;
// Luna is a teenager. Luna loves to read and code. Luna is an e-girl. Luna likes video games\nMe: hello Luna\nLuna: Hello!\n

client.on("ready", function () {
    console.log("Ready!");
    setInterval(() => {
        prompt = defaultPrompt;
    }, 1000 * 60);
});

client.on("message", function (message) {
    try {
        if (message.author.bot) return;
        if (message.content.length > 160 || message.content.length < 1) return;
        if (message.content === "!r") {
            prompt = defaultPrompt;
            return;
        }

        prompt += `Me: ${message.content}\n`;
        (async () => {
            const gptResponse = await openai.complete({
                engine: "curie",
                prompt: prompt,
                maxTokens: 40,
                temperature: 0.8,
                topP: 1,
                presencePenalty: 0.85,
                frequencyPenalty: 0.85,
                bestOf: 1,
                n: 1,
                stream: false,
                stop: ["\n", "\n\n"],
            });
            message.reply(
                `${gptResponse.data.choices[0].text
                    .replace("Luna:", "")
                    .replace("Me:", "")}\n`
            ).catch(() => {
                message.channel.send(
                    `${gptResponse.data.choices[0].text
                        .replace("Luna:", "")
                        .replace("Me:", "")}\n`
                );
            });
            prompt += `${gptResponse.data.choices[0].text.replace("Me:", "Luna:")}\n`;
            console.log(prompt);
        })();
    } catch (e) {
        console.log(e);
    }
});