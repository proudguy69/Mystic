<template >
    <div>
        <input type="text" @input="$emit('inputTitle', $event)" placeholder="Embed Title" @keydown="embedTitle">
        <textarea cols="50" rows="10" @input="$emit('inputDescription',$event)" placeholder="Embed Description"></textarea>
    </div>
</template>


<script>
export default {
    
}
</script>


<style scoped>
    input {
        display: block;
    }
    textarea {
        display: lock;
    }
</style>