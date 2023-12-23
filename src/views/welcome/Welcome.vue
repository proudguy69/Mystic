<template>
    <div class="page_container">
        <div class="section">
            <h1 class="title">Message Builder</h1>
            <button @click="addMessage">+ Add Message</button>
            <div class="forums" v-for="message in messages">
                <MessageForum @inputText="updateText($event, message)"/>
                <button @click="addEmbed(message)">+ Add Embed</button>
                <div class="embeds" v-for="embed in message.embeds">
                    <EmbedForum @inputTitle="updateTitle($event, embed)" @inputDescription="updateDesc($event, embed)"/>
                </div>
            </div>
        </div>

        <div class="section discord">
            <h1 class="title white">Message Preview</h1>
            <div class="messages" v-for="message in messages">
                <Message :message="message"/>
            </div>
        </div>

        <div class="section">
            <VariableSelector />
        </div>
    </div>
</template>


<script>
import Message from './Message.vue'
import MessageForum from './MessageForum.vue'
import EmbedForum from './EmbedForum.vue'
import VariableSelector from './VariableSelector.vue'
export default {
    components: { Message, MessageForum, EmbedForum, VariableSelector},
    data() {
        return {
            messages: []
        }
    },
    methods: {
        addMessage(){
            this.messages.push({
                content: "",
                embeds: []
            })
        },
        addEmbed(message){
            message.embeds.push({
                title: "",
                description: ""
            })
        },
        updateText(event, message){
            message.content = event.target.value
        },
        updateTitle(event, embed) {
            embed.title = event.target.value
        },
        updateDesc(event, embed) {
            embed.description = event.target.value
        }
    }
}
</script>


<style>

    button {
        border-radius: 5px;
        border: 0px;
        padding: 0.5rem;
        background-color: var(--primary_color);
    }
    button:hover {
        background-color: #9990d9;
    }
    .title {
        width: fit-content;
        margin-left: auto;
        margin-right: auto;
        font-size: 24px;
        color: var(--text_color);
    }

    .white {
        color: white;
    }
    :root {
        --background_color: #f4f3fc;
        --background_color2: #e3e2eb;
        --background_color3: #d2d1da;
        --background_discord: #313338;
        --primary_color: #aaa1e8;
        --secondary_color: #cbc6f1;
        --accent_color: #412ebd;
        --text_color: #030208;
        
    }
    body {
        margin: 0px;
        background-color: var(--background_color);
        color: var(--text_color);
        font-family: Arial, Helvetica, sans-serif;
        
    }

    .page_container {
        display: flex;
        gap: 1rem;
        padding: 1rem;
    }
    .section {
        display: block;
        background-color: var(--background_color3);
        width: calc(33vw - 1rem);
        height: calc(100vh - 4rem);
        border-radius: 15px;
        padding: 1rem;
    }

    .discord {
        background-color: var(--background_discord);
        color: white;
    }

    .embed {
        background-color: #2B2D31;
    }
</style>