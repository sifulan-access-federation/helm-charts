var transitionSupported = (function () {
  var s = document.createElement('div').style;
  return ('transition' in s) || ('MozTransition' in s) ||
         ('WebkitTransition' in s) || ('OTransition' in s);
})();

function toggleDs() {
  var e = document.getElementById('wayf_div') || document.all('wayf_div');
  e.className = !e.className ? 'show' : '';
  if (e.className) {
    e.style.visibility = 'visible';
    starttime = new Date().getTime();
    if (transitionSupported) {
      e.removeEventListener('transitionend', hideDs, false);
      e.removeEventListener('webkitTransitionEnd', hideDs, false); 
      e.removeEventListener('oTransitionEnd', hideDs, false); 
      e.addEventListener('transitionend', showDs, false);
      e.addEventListener('webkitTransitionEnd', showDs, false);
      e.addEventListener('oTransitionEnd', showDs, false);
    } else
      e.style.overflow = 'visible';
  } else {
    starttime = new Date().getTime();
    if (transitionSupported) {
      e.removeEventListener('transitionend', showDs, false);
      e.removeEventListener('webkitTransitionEnd', showDs, false);
      e.removeEventListener('oTransitionEnd', showDs, false);
      e.addEventListener('transitionend', hideDs, false);
      e.addEventListener('webkitTransitionEnd', hideDs, false);
      e.addEventListener('oTransitionEnd', hideDs, false);
    } else
      e.style.visibility = 'hidden';
    e.style.overflow = 'hidden';
  }
  return false;
}
var starttime;
function hideDs(e) {
  if (starttime + 100 >= new Date().getTime())
    return;
  if (!this.className) this.style.visibility = 'hidden';
  this.removeEventListener('transitionend', hideDs, false);
  this.removeEventListener('webkitTransitionEnd', hideDs, false);
  this.removeEventListener('oTransitionEnd', hideDs, false);
}
function showDs(e) {
  if (starttime + 100 >= new Date().getTime())
    return;
  if (this.className) this.style.overflow = 'visible';
  this.removeEventListener('transitionend', showDs, false);
  this.removeEventListener('webkitTransitionEnd', showDs, false);
  this.removeEventListener('oTransitionEnd', showDs, false);
}

var appVersion = window.navigator.appVersion.toLowerCase();
if (appVersion.indexOf("msie 6.") == -1 &&
    appVersion.indexOf("msie 7.") == -1) {
  a = document.getElementById("login-link");
  if (a) {
    a.onclick = toggleDs;
  }
}
a = document.getElementById("shibbolethDS");
if (a) {
  a.style.display = "none";
}

