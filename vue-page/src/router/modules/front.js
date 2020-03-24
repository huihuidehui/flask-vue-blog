const Home = () => import("views/front/home/Home");
const Archive = () => import("views/front/archive/Archive");
const About = () => import("views/front/about/About");
const LeWdPel = () => import("views/front/leaveWordsPanel/LeaveWordsPanel");
const ShowPost = () => import("views/front/showPost/ShowPost");
const TagPost = () => import("views/front/tagPost/TagPost.vue");
const CategoryPost = () => import("views/front/categoryPost/CategoryPost.vue");


export default [
  {
    path: "/",
    redirect: "/home/1"
  },
  {
    path: "/home",
    redirect: "/home/1"
  },
  {
    path: "/home/:page",
    component: Home
  },
  {
    path: "/archive",
    component: Archive
  },
  {
    path: "/about",
    component: About
  },
  {
    path: "/guestbook",
    component: LeWdPel
  },
  {
    path: "/showpost/:postUuid",
    component: ShowPost,
    // name:'showpost'
  },
  {
    path: "/tag/post/:tagId/:page",
    component: TagPost
  },
  {
    path:"/category/post/:categoryId",
    redirect:"/category/post/:categoryId/1"
  },
  {
    path: "/category/post/:categoryId/:page",
    component: CategoryPost
  },
  {
    path:"/tag/post/:tagId",
    redirect:"/tag/post/:tagId/1"
  }
]
