FROM node:14.15.1
 WORKDIR /app
 COPY package.json /app/
 RUN npm config set registry "https://registry.npm.taobao.org/" && npm install
 COPY ./ /app
 RUN npm run build
 #指定nginx配置项目，--from=builder 指的是从上一次 build 的结果中提取了编译结果(FROM node:alpine as builder)，即是把刚刚打>    包生成的dist放进nginx中
 FROM nginx
 COPY --from=0 /app/dist /app
 COPY nginx.conf /etc/nginx/nginx.conf
 EXPOSE 80
