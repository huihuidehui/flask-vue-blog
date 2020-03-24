<template>
  <nav class="navbar has-shadow is-spaced" role="navigation" aria-label="main navigation">
    <!-- <div class="container"> -->
    <div class="container column is-four-fifths-widescreen">
      <div class="navbar-brand">
        <slot name="nav-brand"></slot>
      </div>
      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <slot name="nav-menu-start"></slot>
        </div>
        <div class="navbar-end">
          <slot name="nav-menu-end"></slot>
        </div>
      </div>
    </div>
  </nav>
  <!-- <div column></div> -->
  <!-- <div column is-offset-3></div> -->
  <!-- </div> -->
</template>

<script>
document.addEventListener("DOMContentLoaded", () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(
    document.querySelectorAll(".navbar-burger"),
    0
  );

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
      el.addEventListener("click", () => {
        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle("is-active");
        $target.classList.toggle("is-active");
      });
    });
  }
});

export default {
  name: "NavBar",
  data() {
    return {};
  }
};
</script>

<style scoped>
.logo {
  height: 100%;
  border-radius: 100%;
  max-height: 2.4rem;
}
.logo-item {
  padding: 10rem, 10rem;
}
/* .is-spaced{ */
/* padding-top:0; */
/* } */
.column {
  padding-top: 0px;
  padding-bottom: 0px;
}
</style>
