<template>
    <div class="embed-content" v-if="content">
        <div class="embed-title">
            {{embed.title}}
        </div>
        <div class="embed-description">
            {{ embed.description }}
        </div>
    </div>




    <div class="embed" v-else>
        <div class="embed-title">
            {{embed.title}}
        </div>
        <div class="embed-description">
            {{ embed.description }}
        </div>
    </div>
</template>

<script>
export default {
    props: ["embed", "content"]
}
</script>

<style scoped>

    .embed-description {
        font-size: 0.875rem;
        white-space: pre-line;
    }
    .embed-title {
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: white;
    }
    p {
        all: unset;
    }
    .embed {
        margin-bottom: 0.5rem;
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

    .embed-content {
        margin-top: 0.5rem;
        display: inline-block;
        max-width: 520px;
        background-color: rgb(43, 45, 49);
        padding: 8px 16px 16px 12px;
        border-radius: 4px;
        border-left: 4px solid rgb(32, 34, 37);
        display: inline-grid;
        grid-template-columns: auto;
        grid-template-rows: auto;
    }
</style>