<template lang="">
    <div class="message">
        <img src="/src/images/MysticPfp.png" alt="" class="message-img">
        <div class="message-content">
            <div class="content-name">
                <div class="name">Mystic Bot</div> <div class="time">Today at 12:00 AM</div>
            </div>
            <div class="content" v-if="message.content">{{message.content}}</div>
            <div class="embeds" v-else v-for="embed in message.embeds">
        <Embed :embed="embed" :content="true"/>
    </div>
        </div>
    </div>
    <div class="embeds" v-if="message.content" v-for="embed in message.embeds">
        <Embed :embed="embed"/>
    </div>
</template>

<script>
import Embed from './Embed.vue'
export default {
    props: ["message"],
    components: { Embed },
    data() {
        return {
            embeds: [],
            content: ""
        }
    },
    methods: {
    }
}
</script>

<style scoped>

    .content {
    font-size: 1rem;
    margin-bottom: 4px;
    white-space: pre-line;
    }
    .time {
    font-size: 0.75rem;
    color: #979797;
    margin-top: auto;
    }
    .message-content {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    }

    .content-name {
    display: flex;
    gap: 0.5rem;
    }

    .message {
    display: flex;
    gap: 1rem;
    margin-bottom: 0.5rem;
    }

    .message-img {
    height: 48px;
    border-radius: 100px;
    }
</style>