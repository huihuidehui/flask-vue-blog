function formatDate(date) {
  // var y = date.getFullYear();
  // var m = date.getMonth() + 1;
  // m = m < 10 ? ('0' + m) : m;
  // var d = date.getDate();
  // d = d < 10 ? ('0' + d) : d;
  // var h = date.getHours();
  // var minute = date.getMinutes();
  // minute = minute < 10 ? ('0' + minute) : minute;
  // var second = date.getSeconds();
  // second = minute < 10 ? ('0' + second) : second;
  // return y + '-' + m + '-' + d + ' ' + h + ':' + minute + ':' + second;
  return new Date(date)
  // toLocaleString()
};

function _isMobile() {
  let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
  return flag != null;
}

export {formatDate, _isMobile}
