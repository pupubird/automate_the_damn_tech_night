<script>
    import TextInput from "@/components/TextInput.svelte"
    import Dropdown from "@/components/Dropdown.svelte"

    import { storeFE, selectedSpeakers } from '@/components/stores.js';

    export let objAttributes = {};

    let selectedValue;
    let tempValue = "";

    function handleSelect(event) {
        let value = event.detail.value
        
        if (!$selectedSpeakers.includes(value)) {
            if (value != tempValue && tempValue !== "" && tempValue !== null) {
                $selectedSpeakers.pop()
            }
            let l = $selectedSpeakers.length;
            $selectedSpeakers[l] = value
            tempValue = value;

            $storeFE[l].selectedSpeaker = value

            return
        }
        objAttributes.selectedSpeaker = event.detail.value

        selectedValue = null
    }
</script>

<div class="speaker-header-div">
    <p class="speaker-header">Topic #{objAttributes.id}</p>
</div>
<div class="side-by-side">
    <TextInput label="Topic Title" placeholder="Topic Title" bind:instance={objAttributes.topic}/>
    <Dropdown label="Speaker" placeholder="Speaker" 
        items={objAttributes.speakers} bind:selectedValue on:select={handleSelect}/>
</div>
<div>
    <TextInput label="Hook" placeholder="Hook" bind:instance={objAttributes.hook}/>
    <TextInput label="Why" placeholder="Why?" bind:instance={objAttributes.why}/>
    <TextInput label="What" placeholder="What?!" bind:instance={objAttributes.what}/>
</div>

<style>
    .speaker-header-div {
        position: relative;
        margin-bottom: 15px;
        margin-top: 20px;
    }
    .speaker-header {
        font: var(--primary-font-bold);
    }
    .speaker-header:after {
        position: absolute;
        top: 51%;
        left: 100px;
        overflow: hidden;
        width: 87%;
        height: 2px;
        content: '\a0';
        background-color: var(--light-grey)
    }
    .side-by-side {
        display: grid;
        grid-template-columns: auto auto;
        column-gap: 30px
    }
    @media only screen and (max-width: 600px) {
		.speaker-header:after {
            width: 70%;
        }
        .side-by-side {
            display: block
        }
	}
</style>