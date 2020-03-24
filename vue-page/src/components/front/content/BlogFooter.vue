<template>
  <div>
    <footer class="footer">
      <div class="level">
        <div class="level-item has-text-center">
          <div>
            <p class="title">联系我</p>
            <!-- <div> -->
            <div>
              <ul>
                <el-tooltip class="item" effect="light" placement="top">
                  <template v-slot:content>
                    <img class="is-54x74" src="https://s2.ax1x.com/2020/03/06/3qVSpR.png" alt />
                  </template>
                  <li class="list-item">
                    <div class="bgc-weixin">
                      <a v-on:mouseover="addAnimate($event)" v-on:mouseout="removeAnimate($event)">
                        <i class="fa fa-weixin has-text-primary"></i>
                      </a>
                    </div>
                  </li>
                </el-tooltip>
                <el-tooltip class="item" effect="light" placement="top">
                  <template v-slot:content>
                    <img class="is-54x74" src="https://s2.ax1x.com/2020/03/06/3qVSpR.png" alt />
                  </template>
                  <li class="list-item">
                    <!-- <figure class="image bgc is-32x32"> -->

                    <div class="bgc-qq">
                      <a v-on:mouseover="addAnimate($event)" v-on:mouseout="removeAnimate($event)">
                        <i class="fa fa-qq has-text-info"></i>
                      </a>
                    </div>
                    <!-- </figure> -->
                  </li>
                </el-tooltip>
                <li class="list-item">
                  <div class="bgc-github">
                    <a
                      href="https://github.com/laodiaoyadashu"
                      v-on:mouseover="addAnimate($event)"
                      v-on:mouseout="removeAnimate($event)"
                      target="_blank"
                    >
                      <i class="fa fa-github has-text-primary"></i>
                    </a>
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <!-- </div> -->
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "BlogFooter",
  data() {
    return {
      visable: false
    };
  },
  methods: {
    addAnimate($event) {
      $event.currentTarget.className = "animated flipInX";
    },
    removeAnimate($event) {
      $event.currentTarget.className = "";
    }
  }
};
</script>

<style scoped>
.footer {
  background-color: white;
  border-top: 1px solid #c91f37;
  /* width: 100%; */
  margin-top: 4.5rem;
}
.list-item {
  display: inline-block;
  list-style-type: none;
  border-bottom: 0px solid white;
  padding: 0;
  padding-right: 0.5rem;
  margin-top: 1rem;
}
.list-item:not(:last-child) {
  border-bottom: none;
}
.bgc-qq {
  /* padding:1rem */
  padding: 0.3rem 0.556rem;
  background-color: rgba(0, 190, 214, 0.1);
  border-radius: 100%;
}
.bgc-github {
  padding: 0.3rem 0.58rem;
  background-color: #eee;
  border-radius: 100%;
  /* -webkit-backface-visibility: hidden; */
}
.bgc-weixin {
  padding: 0.3rem 0.5rem;
  background-color: #ecfae6;
  border-radius: 100%;
}
.title {
  font-size: 0.9rem;
  line-height: 1rem;
  font-weight: 900;
  padding-left: 0.3rem;
}
.pop-img {
  padding: 0px;
  border: 1px solid #ddd;
}
.is-54x74 {
  width: 108px;
  height: 148px;
}
</style>
