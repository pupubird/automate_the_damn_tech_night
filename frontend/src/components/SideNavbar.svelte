<script>
	import AlertDialog from "@/components/AlertDialog.svelte";
	import Button from "@/components/Button.svelte";

	import Auth from "@/services/auth.js";
	import pushState from "@/utils/pushState";
	
	let pathName = location.pathname;
	export let navs = [
		{
			iconPath: "/assets/icons/home-outline.svg",
			navTitle: "Home",
			navPath: "/home",
		},
		{
			iconPath: "/assets/icons/user.svg",
			navTitle: "Manage Speaker",
			navPath: "/speakers",
		},
		{
			iconPath: "/assets/icons/log-out.svg",
			navTitle: "Logout",
			navPath: "/logout",
		},
	];

	let logoutDialog = false;

	$: active = [
		pathName.includes("/home") ? true : false, pathName.includes("/speakers") ? true : false
	]

	function showLogoutDialog() {
		logoutDialog = true;
	}

	function logout() {
		Auth.logout();
		window.location.href = "/";
	}

	function navigateToPath(path) {
		if (path == "/home") {
			active = [
				true, false
			]
		} else {
			active = [
				false, true
			]
		}
		pushState(path)
	}
</script>

<div class="wrapper">
	<img src="/assets/stc-logo.svg" alt="stc logo" class="stc-icon" />

	{#each navs as nav, i}
		{#if nav.navTitle == "Logout"}
			<div
				class="navigation {pathName.includes(nav.navPath) ? 'active' : ''}"
				id="navigation"
				on:click={showLogoutDialog}
			>
				<img src={nav.iconPath} alt="" class="nav-icon" />
				<p class="nav-title">{nav.navTitle}</p>
			</div>
		{:else}
			<div 
				class="navigation {active[i] ? 'active' : ''}" 
				on:click={navigateToPath(nav.navPath)}>
				<img src={nav.iconPath} alt="" class="nav-icon" />
				<p class="nav-title">{nav.navTitle}</p>
			</div>
		{/if}
	{/each}
</div>

<div class="spacer" />

{#if logoutDialog}
	<AlertDialog bind:visible={logoutDialog}>
		<p class="logout-title">Are you sure?</p>
		<p class="logout-message">Are you sure want to logout?</p>
		<div class="logout-button-div">
			<Button
				secondaryButton
				on:click={() => (logoutDialog = false)}
				label="Cancel"
			/>
			<Button on:click={logout} label="Yes" />
		</div>
	</AlertDialog>
{/if}

<style>
	.spacer {
		min-width: 275px;
		width: 275px;
	}
	.wrapper {
		width: 250px;
		height: 100vh;
		background: #ffffff;
		box-shadow: 4px 24px 22px 13px rgba(0, 0, 0, 0.05);
		padding: 30px 40px;
		position: fixed;
		opacity: 1;
	}
	.stc-icon {
		margin-bottom: 50px;
	}
	.navigation {
		display: flex;
		align-items: center;
		padding: 10px;
		border-radius: 5px;
		margin-bottom: 10px;
		cursor: pointer;
		width: 170px;
		text-decoration: none;
	}
	.active {
		background-color: var(--light-purple-2);
	}
	.nav-icon {
		margin-right: 10px;
	}
	.nav-title {
		font: var(--primary-font-bold);
		font-size: 12px;
		color: var(--purple-1);
	}
	.logout-title {
		font: var(--primary-font-bold);
		font-size: 24px;
		margin-bottom: 20px;
	}
	.logout-message {
		font: var(--primary-font-semibold);
		margin-bottom: 40px;
	}
	.logout-button-div {
		display: grid;
		grid-template-columns: auto auto;
		column-gap: 30px;
	}
	@media only screen and (max-width: 600px) {
		.logout-button-div {
			display: block;
		}
	}
</style>
