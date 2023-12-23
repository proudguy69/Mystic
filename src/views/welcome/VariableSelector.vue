<template>
    <div class="selector">
        <ul v-for="option in options" id="options">
            <li>{{option}}</li>  
        </ul>
    </div>
</template>


<script defer>
export default {
    data(){
        return {
            options: ["{user}", "{user.mention}", "{server.name}"],
            selected: null
        }
    },
    methods: {
        match(x){
            return x == this.selected
        }
    },
    mounted(){
        this.selected = this.options[0]
        const options = document.getElementById("options")
        //options.children[this.options.findIndex(this.match)+1].classList.add("selected")

        document.addEventListener("keydown", (e) =>{
            if (e.key == "ArrowDown") {
                this.selected = this.options[this.options.findIndex(this.match)+1]
                console.log(options.children)
            } else if (e.key == "ArrowUp") {
                this.selected = this.options[this.options.findIndex(this.match)-1]
            }
        })
    },
    updated(){
        console.log("updated!")
    }
}
</script>


<style scoped>
.selector {
    display: inline-block;
    background-color: var(--text_color);
    color: white;
    width: fit-content;
    padding: 0.25rem;
    border-radius: 5px;
}

h1 {
    all: unset;
}

ul, li {
    all: unset;
}

ul {
    display: flex;
    flex-direction: column;
}

li {
    padding: 0.1rem;
    border-radius: 2px;
}

.selected {
    background-color: rgb(83, 83, 83);
}
</style>