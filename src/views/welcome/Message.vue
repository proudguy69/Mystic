<template lang="">
    <div class="message">
        <img src="/src/images/MysticPfp.png" alt="" class="message-img">
        <div class="message-content">
            <div class="content-name">
                <div class="name">Mystic Bot</div> <div class="time">Today at 12:00 AM</div>
            </div>
            <div class="content">Hello World..!</div>
        </div>
    </div>
    <div class="embeds">
        <div class="embed">
            <div class="title">
                Hello World
            </div>
            <div class="description">
                This is my special Embed
            </div>
        </div>
    </div>
</template>



<style scoped>
    .description {
        font-size: 0.875rem;
    }
    .title {
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    p {
        all: unset;
    }
    .embed {
        display: inline-block;
        max-width: 520px;
        background-color: rgb(43, 45, 49);
        padding: 8px 16px 16px 12px;
        margin-left: calc(48px + 1rem);
        border-radius: 4px;
        border-left: 4px solid rgb(32, 34, 37);
        display: inline-grid;
        grid-template-columns: auto;
        grid-template-rows: auto;
    }
    .content {
    font-size: 1rem;
    margin-bottom: 4px;
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
    }

    .message-img {
    height: 48px;
    border-radius: 100px;
    }
</style>