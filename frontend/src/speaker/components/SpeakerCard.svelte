<script>
    import Card from "@/components/Card.svelte"
    import pushState from "@/utils/pushState";

    export let speaker = {
        name: "Rain Chai Chang Cheng Cheng",
        position: "STC Head of MarketingSTC Head of Marketing",
        avatar: "/assets/example-avatar.png"
    }

    function nagivateEvent(id) {
        pushState(`/speakers/speaker/${id}`)
    }
</script>

<div class="card-wrapper" on:click={nagivateEvent(speaker.id)}>
    <Card>
        <div class="wrapper">
            <img src={speaker.avatar} alt="" class="avatar"/>
            <div>
                <p class="speaker-name">{speaker.name}</p>
                <p class="speaker-position">{speaker.position}</p>
            </div>
            <img src="/assets/icons/edit.svg" alt="" class="edit-icon"/>
        </div>
    </Card>
</div>

<style>
    .card-wrapper {
        width: 300px;
        margin-right: 30px;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .wrapper {
        padding: 20px;
        display: flex;
        align-items: center;
        position: relative;
    }
    .avatar {
        width: 64px;
        border-radius: 50%;
        margin-right: 20px;
    }
    .speaker-name {
        font: var(--primary-font-bold);
        font-size: 14px;
        max-width: 150px;
        word-wrap: break-word;
    }
    .speaker-position {
        color: var(--dark-grey);
        font-size: 12px;
    }
    .edit-icon {
        position: absolute;
        right: 20px;
        top: 20px;
        width: 18px;
    }
    @media only screen and (max-width: 600px) {
		.card-wrapper {
            width: 300px;
        }
	}
</style>