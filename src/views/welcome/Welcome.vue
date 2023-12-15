<template>
    <div class="page_container">
        <div class="section"></div>
        <div class="section discord">
        <Message/>
        </div>
        <div class="section"></div>
    </div>
</template>


<script>
import Message from './Message.vue'
export default {
components: { Message }
}
</script>


<style>
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