const Login = () => import("views/admin/login/Login.vue");
const Index = () => import("views/admin/index/Index.vue");
const CreatePost = () => import("views/admin/post/CreatePost.vue");
const EditorPost = () => import("views/admin/post/EditorPost.vue");
const ManagePost = () => import("views/admin/post/ManagePost.vue");
const Base = () => import("views/admin/Base.vue")
const CreateCategory = () => import("views/admin/category/CreateCategory.vue");
const ManageCategory = () => import("views/admin/category/ManageCategory.vue");
const EditCategory = () => import("views/admin/category/EditCategory.vue");
const CreateTag = () => import("views/admin/tag/CreateTag.vue");
const ManageTag = () => import("views/admin/tag/ManageTag.vue");
const EditTag = () => import("views/admin/tag/EditTag.vue");
const EditAbout = () => import("views/admin/about/EditAbout.vue");
export default [
  {
    path: "/admin",
    redirect: "/admin/index"
  },
  {
    path: "/admin",
    components: {
      admin: Base
    },
    children: [{
      path: "index",
      component: Index,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "article/create",
      component: CreatePost,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "article/managepost",
      component: ManagePost,
      meta: {
        requireAuth: true
      }
    },
    {
      // path: "article/edit/:uuid",
      path: "article/edit",
      component: EditorPost,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "category/create",
      component: CreateCategory,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "category/edit",
      component: EditCategory,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "category/manage",
      component: ManageCategory,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "tag/create",
      component: CreateTag,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "tag/edit",
      component: EditTag,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "tag/manage",
      component: ManageTag,
      meta: {
        requireAuth: true
      }
    },
    {
      path: "about",
      component: EditAbout,
      meta: {
        requireAuth: true
      }
    }
    ]
  },
  {
    path: "/admin/login",
    components: {
      admin: Login
    }
  },
]
