<!DOCTYPE html><html lang='en' class='no-js'>
<head><script src='//static.codepen.io/assets/editor/live/console_runner-ce3034e6bde3912cc25f83cccb7caa2b0f976196f2f2d52303a462c826d54a73.js'></script><script src='//static.codepen.io/assets/editor/live/css_reload-2a5c7ad0fe826f66e054c6020c99c1e1c63210256b6ba07eb41d7a4cb0d0adab.js'></script><meta charset='UTF-8'><meta name="robots" content="noindex"><link rel="shortcut icon" type="image/x-icon" href="//static.codepen.io/assets/favicon/favicon-8ea04875e70c4b0bb41da869e81236e54394d63638a1ef12fa558a4a835f1164.ico" /><link rel="mask-icon" type="" href="//static.codepen.io/assets/favicon/logo-pin-f2d2b6d2c61838f7e76325261b7195c27224080bc099486ddd6dccb469b8e8e6.svg" color="#111" /><link rel="canonical" href="https://codepen.io/JoshuaMorris/pen/ojNQLN" />
<meta name="viewport" content="width=device-width">
<script>(function(H){H.className=H.className.replace(/\bno-js\b/,'js')})(document.documentElement);</script>
<meta name="author" content="Joshua Morris <me@joshuamorris.info>" />
<script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');ga('create', 'UA-65924910-1', 'auto');ga('send', 'pageview');</script>
<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css'>
<style class="cp-pen-styles">@import url(https://fonts.googleapis.com/css?family=Ubuntu);
html {
  box-sizing: border-box;
}

*, *::after, *::before {
  box-sizing: inherit;
}

body {
  font-family: Ubuntu, sans-serif;
  background-color: #666;
  width: 100%;
  position: absolute;
  height: auto;
  min-height: 100% !important;
}
body .background-image-cont div {
  transition: all 1.5s ease-in-out;
  width: 100%;
  position: absolute;
  height: auto;
  min-height: 100% !important;
  background-color: #666;
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  background-size: cover;
  opacity: 1;
  top: 0;
}
body .background-image-cont div.fade-out {
  transition: all 1.5s ease-in-out;
  opacity: 0;
}
body a {
  transition: color 0.5s ease-in-out;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.9);
}
body a:hover {
  color: gold;
  color: rgba(255, 215, 0, 0.7);
}
body .container {
  background-color: #4d4d4d;
  background-color: rgba(0, 0, 0, 0.7);
  -webkit-animation: moveInDown 0.9s ease-in-out forwards;
  animation: moveInDown 0.9s ease-in-out forwards;
  -webkit-animation-delay: 1s;
  animation-delay: 1s;
  display: block;
  text-align: center;
  color: #fff;
  border-radius: 1%;
  border: 1px solid #000;
  position: static;
  opacity: 1;
  margin: 0 auto;
  height: -webkit-fit-content;
  height: -moz-fit-content;
  height: fit-content;
  z-index: 0;
}
body .container::after {
  clear: both;
  content: "";
  display: block;
}
@media screen and (min-width: 20em) {
  body .container {
    -webkit-transform-origin: 50%;
    transform-origin: 50%;
    opacity: 0;
    width: 90%;
    margin-top: 10%;
    margin-bottom: 25%;
  }
}
@media screen and (min-width: 45em) {
  body .container {
    width: 75%;
    margin-bottom: 10%;
  }
}
@media screen and (min-width: 60em) {
  body .container {
    width: 50%;
  }
}
body .container .header-logo {
  margin-bottom: 0.5em;
  position: relative;
  margin: 0 auto;
  background-color: transparent;
  z-index: 0;
  overflow: visible;
}
@media screen and (min-width: 20em) {
  body .container .header-logo {
    height: 15em;
    width: 15em;
  }
}
@media screen and (min-width: 45em) {
  body .container .header-logo {
    height: 33em;
    width: 33em;
  }
}
body .container .header-logo div {
  transition: background 0.5s ease-in-out, -webkit-clip-path 0.5s ease-in-out;
  transition: background 0.5s ease-in-out, clip-path 0.5s ease-in-out;
  transition: background 0.5s ease-in-out, clip-path 0.5s ease-in-out, -webkit-clip-path 0.5s ease-in-out;
  width: 100%;
  height: 100%;
  margin: 0 auto;
  background-repeat: no-repeat;
  background-position: top center;
  background-size: cover;
  background-clip: content-box;
  position: absolute;
  overflow: visible;
}
body .container .header-logo div:nth-child(1) {
  background-color: transparent;
  background-position: center center;
  margin: 15% 15%;
  height: 70%;
  width: 70%;
  z-index: 9999;
  opacity: 1;
}
@media screen and (min-width: 20em) {
  body .container .header-logo div:nth-child(1) {
    border-radius: 100%;
    background-clip: padding-box;
  }
}
body .container .header-logo div:nth-child(2) {
  background-color: rgba(255, 0, 0, 0.4);
  background-color: rgba(255, 0, 0, 0.4);
  z-index: 3;
  opacity: 0;
  -webkit-animation: image-jazz 1s infinite, hide 1s forwards, shrink2 2.5s forwards;
  animation: image-jazz 1s infinite, hide 1s forwards, shrink2 2.5s forwards;
}
body .container .header-logo div:nth-child(3) {
  background-color: rgba(255, 165, 0, 0.4);
  background-color: rgba(255, 165, 0, 0.4);
  z-index: 4;
  opacity: 0;
  -webkit-animation: image-jazz 1s infinite, hide 1s forwards, shrink3 2.5s forwards;
  animation: image-jazz 1s infinite, hide 1s forwards, shrink3 2.5s forwards;
}
body .container .header-logo div:nth-child(4) {
  background-color: rgba(255, 215, 0, 0.4);
  background-color: rgba(255, 215, 0, 0.4);
  z-index: 5;
  opacity: 0;
  -webkit-animation: image-jazz 1s infinite, hide 1s forwards, shrink4 2.5s forwards;
  animation: image-jazz 1s infinite, hide 1s forwards, shrink4 2.5s forwards;
}
body .container .header-logo div:nth-child(5) {
  background-color: rgba(255, 255, 0, 0.4);
  background-color: rgba(255, 255, 0, 0.4);
  z-index: 2;
  opacity: 0;
  -webkit-animation: image-jazz 1s infinite, hide 1s forwards, shrink5 2.5s forwards;
  animation: image-jazz 1s infinite, hide 1s forwards, shrink5 2.5s forwards;
}
body .container .header-logo:hover div:nth-child(2), body .container .header-logo:focus div:nth-child(2) {
  -webkit-animation: image-jazz 1s infinite, grow2 1.3s forwards, show 1s forwards;
  animation: image-jazz 1s infinite, grow2 1.3s forwards, show 1s forwards;
}
body .container .header-logo:hover div:nth-child(3), body .container .header-logo:focus div:nth-child(3) {
  -webkit-animation: image-jazz 1s infinite, grow3 1.2s forwards, show 2s forwards;
  animation: image-jazz 1s infinite, grow3 1.2s forwards, show 2s forwards;
}
body .container .header-logo:hover div:nth-child(4), body .container .header-logo:focus div:nth-child(4) {
  -webkit-animation: image-jazz 1s infinite, grow4 1.1s forwards, show 3s forwards;
  animation: image-jazz 1s infinite, grow4 1.1s forwards, show 3s forwards;
}
body .container .header-logo:hover div:nth-child(5), body .container .header-logo:focus div:nth-child(5) {
  -webkit-animation: image-jazz 1s infinite, grow5 1.1s forwards, show 3s forwards;
  animation: image-jazz 1s infinite, grow5 1.1s forwards, show 3s forwards;
}
body .container .lead {
  margin: 0 auto;
}
body .container .lead::after {
  clear: both;
  content: "";
  display: block;
}
@media screen and (min-width: 20em) {
  body .container .lead {
    max-width: 85%;
  }
}
@media screen and (min-width: 60em) {
  body .container .lead {
    max-width: 75%;
  }
}
body .container .lead h1 {
  margin: 0;
  font-size: 2.5em;
}
body .container .lead h2 {
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  font-size: 0.75em;
}
@media screen and (min-width: 20em) {
  body .container .lead h2 {
    padding-bottom: 0.25em;
    margin: 0 0 0.25em 0;
  }
}
@media screen and (min-width: 45em) {
  body .container .lead h2 {
    padding-bottom: 0.5em;
    margin: 0 0 0.5em 0;
  }
}
@media screen and (min-width: 20em) {
  body .container .lead p {
    line-height: 1em;
    margin-bottom: 1em;
  }
}
@media screen and (min-width: 45em) {
  body .container .lead p {
    line-height: 1.5em;
    margin-bottom: 1.5em;
  }
}
body .container .links {
  margin: 0 auto;
  margin-bottom: 2em;
}
body .container .links::after {
  clear: both;
  content: "";
  display: block;
}
@media screen and (min-width: 20em) {
  body .container .links {
    max-width: 85%;
  }
}
@media screen and (min-width: 45em) {
  body .container .links {
    max-width: 75%;
  }
}
body .container .links ul {
  margin: 0;
}
body .container .links ul li {
  display: inline-block;
  width: 4em;
  list-style: none;
  padding-right: 3em;
}
body .container .links ul li .svg-icon {
  transition: all 0.25s ease-in-out;
  position: relative;
  border-radius: 100%;
  height: 4em;
  width: 4em;
  color: #fff;
  fill: #fff;
  display: block;
}
body .container .links ul li .svg-icon svg {
  width: 100%;
  height: 100%;
}
body .container .links ul li .svg-icon em {
  font-size: 14px;
  line-height: 1.5;
  margin-top: -.75em;
  position: absolute;
  text-align: center;
  top: 50%;
  right: 0;
  bottom: 0;
  left: 0;
}
body .container .links ul li .svg-icon:hover {
  background: gold;
  background: rgba(255, 215, 0, 0.7);
}
body .loader {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  transition-delay: 1.5s;
  position: fixed;
  bottom: 1em;
  right: 2em;
  opacity: 1;
  z-index: 1;
}
body .loader .loader-inner {
  bottom: 0;
  height: 60px;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
  width: 100px;
}
body .loader .loader-inner .loader-line-wrap {
  -webkit-animation: spin 2000ms cubic-bezier(0.175, 0.885, 0.32, 1.275) infinite;
  animation: spin 2000ms cubic-bezier(0.175, 0.885, 0.32, 1.275) infinite;
  box-sizing: border-box;
  height: 50px;
  left: 0;
  overflow: hidden;
  position: absolute;
  top: 0;
  /*transform-origin: 50% 100%;*/
  -webkit-transform-origin: 50% 100%;
  transform-origin: 50% 100%;
  width: 100px;
}
body .loader .loader-inner .loader-line-wrap .loader-line {
  border: 4px solid transparent;
  border-radius: 100%;
  box-sizing: border-box;
  height: 100px;
  left: 0;
  margin: 0 auto;
  position: absolute;
  right: 0;
  top: 0;
  width: 100px;
}
body .loader .loader-inner .loader-line-wrap:nth-child(1) {
  -webkit-animation-delay: -50ms;
          animation-delay: -50ms;
}
body .loader .loader-inner .loader-line-wrap:nth-child(1) .loader-line {
  border-color: #eb4747;
  height: 90px;
  width: 90px;
  top: 7px;
}
body .loader .loader-inner .loader-line-wrap:nth-child(2) {
  -webkit-animation-delay: -100ms;
          animation-delay: -100ms;
}
body .loader .loader-inner .loader-line-wrap:nth-child(2) .loader-line {
  border-color: #ebeb47;
  height: 76px;
  width: 76px;
  top: 14px;
}
body .loader .loader-inner .loader-line-wrap:nth-child(3) {
  -webkit-animation-delay: -150ms;
          animation-delay: -150ms;
}
body .loader .loader-inner .loader-line-wrap:nth-child(3) .loader-line {
  border-color: #47eb47;
  height: 62px;
  width: 62px;
  top: 21px;
}
body .loader .loader-inner .loader-line-wrap:nth-child(4) {
  -webkit-animation-delay: -200ms;
          animation-delay: -200ms;
}
body .loader .loader-inner .loader-line-wrap:nth-child(4) .loader-line {
  border-color: #47ebeb;
  height: 48px;
  width: 48px;
  top: 28px;
}
body .loader .loader-inner .loader-line-wrap:nth-child(5) {
  -webkit-animation-delay: -250ms;
          animation-delay: -250ms;
}
body .loader .loader-inner .loader-line-wrap:nth-child(5) .loader-line {
  border-color: #4747eb;
  height: 34px;
  width: 34px;
  top: 35px;
}
body .loader.ng-hide-remove {
  opacity: 0;
  display: block !important;
}
body .loader.ng-hide-remove.ng-hide-remove-active {
  opacity: 1;
}

.bg-cred {
  background-color: #333333;
  background-color: rgba(0, 0, 0, 0.8);
  transition: all 0.5s ease-in-out;
  color: #666;
  position: absolute;
  bottom: 0;
  font-size: 0.7em;
  width: 100%;
  margin: 0 auto;
  text-align: center;
  z-index: 0;
  opacity: 1;
}
.bg-cred p:first-child {
  padding-bottom: 2px;
}

.bg-cred.ng-hide-add,
.bg-cred.ng-hide-remove {
  transition: all 0.5s linear;
}

.bg-cred.ng-hide {
  opacity: 0;
}

.js body .logo img {
  display: none;
}
.js body .nojs-notice {
  display: none;
}

.tt {
  position: absolute;
  box-sizing: border-box;
  margin-top: 0.5em;
  background-color: #ccac00;
  cursor: default;
  visibility: hidden;
  border: 0 solid false;
  color: #000;
  left: 50%;
  top: 100%;
  width: 6em;
  margin-left: -3em;
  padding: .5em .75em;
  /*box-shadow: 0 .05em .15em rgba($highlight-color, .1);*/
}
.tt:after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 50%;
  width: 0;
  height: 0;
  height: 0;
  width: 0;
  border-bottom: 0.5em solid #ccac00;
  border-left: 0.5em solid transparent;
  border-right: 0.5em solid transparent;
  margin-left: -0.5em;
}
.tt:before {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 50%;
  width: 0;
  height: 0;
  height: 0;
  width: 0;
  border-bottom: 0.5em solid #ccac00;
  border-left: 0.5em solid transparent;
  border-right: 0.5em solid transparent;
  margin-left: -0.5em;
}

.tt-a {
  position: relative;
}
.tt-a:hover .tt {
  -webkit-animation: tooltip-animation 0.3s;
  animation: tooltip-animation 0.3s;
  background-color: #ffdf33;
  background-color: rgba(255, 215, 0, 0.8);
  visibility: visible;
}

.no-js body {
  background-image: url(https://upload.wikimedia.org/wikipedia/commons/7/79/Tower_Bridge_Sacramento_edit.jpg);
}
.no-js body .logo img {
  display: block;
  height: 25em;
  width: 25em;
  margin: 3em auto 0;
}
.no-js body .loader {
  display: none;
  width: 33em;
  height: 33em;
}
.no-js body .bg-cred {
  display: none;
}
.no-js body .nojs-notice {
  position: absolute;
  top: 0;
  width: 100%;
  margin: 0 auto;
  text-align: center;
  background-color: gold;
  background-color: rgba(255, 215, 0, 0.7);
}



@-webkit-keyframes moveInDown {
  0% {
    -webkit-transform: translate3d(0, -500px, 0);
  }
  60% {
    -webkit-transform: translate3d(0, 12px, 0);
  }
  80% {
    -webkit-transform: translate3d(0, -8px, 0);
  }
  100% {
    -webkit-transform: translate3d(0, 0, 0);
    opacity: 1;
  }
}
@keyframes moveInDown {
  0% {
    -webkit-transform: translate3d(0, -500px, 0);
    transform: translate3d(0, -500px, 0);
  }
  60% {
    -webkit-transform: translate3d(0, 12px, 0);
    transform: translate3d(0, 12px, 0);
  }
  80% {
    -webkit-transform: translate3d(0, -8px, 0);
    transform: translate3d(0, -8px, 0);
  }
  100% {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    opacity: 1;
  }
}
@-webkit-keyframes grow5 {
  0% {
    -webkit-transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1, 1);
  }
}
@keyframes grow5 {
  0% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1, 1);
    transform: scale(1, 1);
  }
}
@-webkit-keyframes grow4 {
  0% {
    -webkit-transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1.2, 1.2);
  }
}
@keyframes grow4 {
  0% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1.2, 1.2);
    transform: scale(1.2, 1.2);
  }
}
@-webkit-keyframes grow3 {
  0% {
    -webkit-transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1.4, 1.4);
  }
}
@keyframes grow3 {
  0% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1.4, 1.4);
    transform: scale(1.4, 1.4);
  }
}
@-webkit-keyframes grow2 {
  0% {
    -webkit-transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1.6, 1.6);
  }
}
@keyframes grow2 {
  0% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
  100% {
    -webkit-transform: scale(1.6, 1.6);
    transform: scale(1.6, 1.6);
  }
}
@-webkit-keyframes shrink5 {
  0% {
    -webkit-transform: scale(1, 1);
  }
  100% {
    -webkit-transform: scale(0, 0);
  }
}
@keyframes shrink5 {
  0% {
    -webkit-transform: scale(1, 1);
    transform: scale(1, 1);
  }
  100% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
}
@-webkit-keyframes shrink4 {
  0% {
    -webkit-transform: scale(1.2, 1.2);
  }
  100% {
    -webkit-transform: scale(0, 0);
  }
}
@keyframes shrink4 {
  0% {
    -webkit-transform: scale(1.2, 1.2);
    transform: scale(1.2, 1.2);
  }
  100% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
}
@-webkit-keyframes shrink3 {
  0% {
    -webkit-transform: scale(1.4, 1.4);
  }
  100% {
    -webkit-transform: scale(0, 0);
  }
}
@keyframes shrink3 {
  0% {
    -webkit-transform: scale(1.4, 1.4);
    transform: scale(1.4, 1.4);
  }
  100% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
}
@-webkit-keyframes shrink2 {
  0% {
    -webkit-transform: scale(1.6, 1.6);
  }
  100% {
    -webkit-transform: scale(0, 0);
  }
}
@keyframes shrink2 {
  0% {
    -webkit-transform: scale(1.6, 1.6);
    transform: scale(1.6, 1.6);
  }
  100% {
    -webkit-transform: scale(0, 0);
    transform: scale(0, 0);
  }
}
@-webkit-keyframes show {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@keyframes show {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@-webkit-keyframes hide {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@keyframes hide {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@-webkit-keyframes spin {
  0%,
  15% {
    -webkit-transform: rotate(0);
  }
  100% {
    -webkit-transform: rotate(20deg);
  }
}
@keyframes spin {
  0%,
  15% {
    -webkit-transform: rotate(0);
    transform: rotate(0);
  }
  100% {
    -webkit-transform: rotate(20deg);
    transform: rotate(20deg);
  }
}
body .container .links ul li .svg-icon:hover {
  transition: background-color 0.5s ease, color 0.5s ease-in-out, -webkit-transform 0.5s ease-out;
  transition: background-color 0.5s ease, transform 0.5s ease-out, color 0.5s ease-in-out;
  transition: background-color 0.5s ease, transform 0.5s ease-out, color 0.5s ease-in-out, -webkit-transform 0.5s ease-out;
  -webkit-transform: scale(1.25);
  transform: scale(1.25);
  border-radius: 100%;
  color: #000;
  fill: #000;
}
</style></head><body>
<body id="ng-app" data-ng-app="app">
  <div class="background-image-cont" data-Rbackground="https://www.reddit.com/r/earthporn/top.json" data-request-limit="50" data-auto="true">
    <div data-background-image-preload="https://cdn.joshuamorris.info/assets/images/tower-bridge-sacramento-public-domain.444a5e44.jpg"></div>
  </div>
  <section class="container" role="contentinfo">
  <div class="header-logo">
    <div class="logo" data-background-image-preload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5926/profile/profile-512.jpg"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5926/profile/profile-512.jpg" /></div>
    <div class="ray"></div>
    <div class="ray"></div>
    <div class="ray"></div>
    <div class="ray"></div>
  </div>
  <div class="lead">
    <h1><a href="https://www.joshuamorris.info" target="_blank">Joshua Morris</a></h1>
    <h2></h2>
    <p>Full Stack Software Engineer<br />Fluent in Javascript, Node.js, C/C++, Ruby, PHP, HTML5 and CSS3.</p>
  </div>
  <div class="links">
    <ul>
      <li>
        <a class="svg-icon tt-a" href="https://github.com/JoshuaMorris/" target="_blank">
          <svg viewBox="0 0 512 512">
              <path d="M256 70.7c-102.6 0-185.9 83.2-185.9 185.9 0 82.1 53.3 151.8 127.1 176.4 9.3 1.7 12.3-4 12.3-8.9V389.4c-51.7 11.3-62.5-21.9-62.5-21.9 -8.4-21.5-20.6-27.2-20.6-27.2 -16.9-11.5 1.3-11.3 1.3-11.3 18.7 1.3 28.5 19.2 28.5 19.2 16.6 28.4 43.5 20.2 54.1 15.4 1.7-12 6.5-20.2 11.8-24.9 -41.3-4.7-84.7-20.6-84.7-91.9 0-20.3 7.3-36.9 19.2-49.9 -1.9-4.7-8.3-23.6 1.8-49.2 0 0 15.6-5 51.1 19.1 14.8-4.1 30.7-6.2 46.5-6.3 15.8 0.1 31.7 2.1 46.6 6.3 35.5-24 51.1-19.1 51.1-19.1 10.1 25.6 3.8 44.5 1.8 49.2 11.9 13 19.1 29.6 19.1 49.9 0 71.4-43.5 87.1-84.9 91.7 6.7 5.8 12.8 17.1 12.8 34.4 0 24.9 0 44.9 0 51 0 4.9 3 10.7 12.4 8.9 73.8-24.6 127-94.3 127-176.4C441.9 153.9 358.6 70.7 256 70.7z"/>
            </svg>
          <!--[if lt IE 9]><em>GitHub</em><![endif]-->
          <span class="tt">GitHub</span>
        </a>
      </li>
      <li>
        <a class="svg-icon tt-a" href="https://www.linkedin.com/in/~joshuamorris/" target="_blank">
          <svg viewBox="0 0 512 512">
              <path d="M186.4 142.4c0 19-15.3 34.5-34.2 34.5 -18.9 0-34.2-15.4-34.2-34.5 0-19 15.3-34.5 34.2-34.5C171.1 107.9 186.4 123.4 186.4 142.4zM181.4 201.3h-57.8V388.1h57.8V201.3zM273.8 201.3h-55.4V388.1h55.4c0 0 0-69.3 0-98 0-26.3 12.1-41.9 35.2-41.9 21.3 0 31.5 15 31.5 41.9 0 26.9 0 98 0 98h57.5c0 0 0-68.2 0-118.3 0-50-28.3-74.2-68-74.2 -39.6 0-56.3 30.9-56.3 30.9v-25.2H273.8z"/>
            </svg>
          <!--[if lt IE 9]><em>LinkedIn</em><![endif]-->
          <span class="tt">LinkedIn</span>
        </a>
      </li>
      <li>
        <a class="svg-icon tt-a" href="https://codepen.io/JoshuaMorris/" target="_blank">
          <svg viewBox="0 0 512 512">
              <path d="M427 201.9c-0.6-4.2-2.9-8-6.4-10.3L264.2 87.3c-4.9-3.3-11.4-3.3-16.3 0L91.4 191.6c-4 2.7-6.5 7.4-6.5 12.2v104.3c0 4.8 2.5 9.6 6.5 12.2l156.4 104.3c4.9 3.3 11.4 3.3 16.3 0L420.6 320.4c4-2.6 6.6-7.4 6.6-12.2V203.9C427.1 203.2 427.1 202.6 427 201.9 427 201.7 427.1 202.6 427 201.9zM270.7 127.1l115.2 76.8 -51.5 34.4 -63.8-42.7V127.1zM241.3 127.1v68.6l-63.8 42.7 -51.5-34.4L241.3 127.1zM114.3 231.4l36.8 24.6 -36.8 24.6V231.4zM241.3 384.9L126.1 308.1l51.5-34.4 63.8 42.6V384.9zM256 290.8l-52-34.8 52-34.8 52 34.8L256 290.8zM270.7 384.9V316.3l63.8-42.6 51.5 34.4L270.7 384.9zM397.7 280.6l-36.8-24.6 36.8-24.6V280.6z"/>
            </svg>
          <!--[if lt IE 9]><em>CodePen</em><![endif]-->
          <span class="tt">CodePen</span>
        </a>
      </li>
      <li>
        <a class="svg-icon tt-a" href="https://twitter.com/TheWoollyBully" target="_blank">
          <svg viewBox="0 0 512 512">
              <path d="M419.6 168.6c-11.7 5.2-24.2 8.7-37.4 10.2 13.4-8.1 23.8-20.8 28.6-36 -12.6 7.5-26.5 12.9-41.3 15.8 -11.9-12.6-28.8-20.6-47.5-20.6 -42 0-72.9 39.2-63.4 79.9 -54.1-2.7-102.1-28.6-134.2-68 -17 29.2-8.8 67.5 20.1 86.9 -10.7-0.3-20.7-3.3-29.5-8.1 -0.7 30.2 20.9 58.4 52.2 64.6 -9.2 2.5-19.2 3.1-29.4 1.1 8.3 25.9 32.3 44.7 60.8 45.2 -27.4 21.4-61.8 31-96.4 27 28.8 18.5 63 29.2 99.8 29.2 120.8 0 189.1-102.1 185-193.6C399.9 193.1 410.9 181.7 419.6 168.6z"/>
            </svg>
          <!--[if lt IE 9]><em>Twitter</em><![endif]-->
          <span class="tt">Twitter</span>
        </a>
      </li>
    </ul>
  </div>
</section>
<section class="loader" data-ng-show="loading">
  <div class="loader-inner">
    <div class="loader-line-wrap">
      <div class="loader-line"></div>
    </div>
    <div class="loader-line-wrap">
      <div class="loader-line"></div>
    </div>
    <div class="loader-line-wrap">
      <div class="loader-line"></div>
    </div>
    <div class="loader-line-wrap">
      <div class="loader-line"></div>
    </div>
    <div class="loader-line-wrap">
      <div class="loader-line"></div>
    </div>
  </div>
</section>
  <div class="bg-cred" data-ng-show="!bg">
    <p><em>View from the east side of the Sacramento River as it flows through the city of Sacramento.</em><br />Background photo courtesy of Michael Grindstaff of Sacramento, CA released on <a href="https://commons.wikimedia.org/wiki/File:Tower_Bridge_Sacramento_edit.jpg" target="_blank">Wikipedia</a></p>
  </div>
  <div class="bg-cred" data-ng-show="bg">
    <p><em data-ng-bind="bg.title"></em><br /><span data-ng-if="bg.show">Background photo uploaded to <a data-ng-href="{{bg.link}}" target="_blank" data-ng-bind="bg.subreddit"></a> by </span><a data-ng-href="{{bg.authorLink}}" target="_blank" data-ng-bind="bg.author"></a></p>
  </div>
  <div class="nojs-notice">
    <p>For a better experience, please enable JavaScript in your browser.</p>
  </div>
</body>
<script src='//static.codepen.io/assets/common/stopExecutionOnTimeout-41c52890748cd7143004e05d3c5f786c66b19939c4500ce446314d1748483e13.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-animate.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-aria.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-cookies.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-resource.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-route.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-sanitize.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-touch.min.js'></script><script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-loader.min.js'></script>
<script >(function (angular) {
  'use strict';
  var module = angular.module('app', [
  'ngAnimate',
  'ngTouch']);


  module.directive('backgroundImagePreload', ['$imagePreload', function ($imagePreload) {
    return {
      'restrict': 'A',
      'link': function (scope, element, attr) {
        if (!attr.backgroundImagePreload) return;
        $imagePreload(attr.backgroundImagePreload).then(function () {
          element.css({
            'background-image': 'url(' + attr.backgroundImagePreload + ')' });

        });
      } };

  }]);

  module.factory('$imagePreload', ['$q', function ($q) {
    return function (url) {
      var deferred = $q.defer(),
      img = new Image();
      img.src = url;

      if (img.complete) {
        deferred.resolve();
      } else {
        img.addEventListener('load', function () {
          deferred.resolve();
        });

        img.addEventListener('error', function () {
          deferred.reject();
        });
      }

      return deferred.promise;
    };
  }]);

  module.directive('background', ['$http', '$log', '$interval', '$imagePreload', '$window', '$animate', '$timeout', '$compile', function ($http, $log, $interval, $imagePreload, $window, $animate, $timeout, $compile) {
    return {
      'restrict': 'A',
      'scope': '=',
      'link': function (scope, element, attr) {
        scope.window = angular.element($window);
        scope.bgProcess = undefined;
        scope.assets = [];
        scope.auto = attr.auto ? true : false;
        scope.config = {
          method: 'GET',
          url: attr.background ? attr.background + '?limit=' + attr.requestLimit : 'https://www.reddit.com/r/earthporn/top.json?limit=50' };


        scope.getWindowDimensions = function () {
          return {
            'h': $window.innerHeight,
            'w': $window.innerWidth };

        };

        scope.$watch(scope.getWindowDimensions, function (n) {
          if (!n) {
            return;
          }

          scope.height = n.h;
          scope.width = n.w;

          // $log.debug('width X height:', scope.height, scope.width);
        }, true);

        scope.window.bind('resize', function () {
          scope.$apply();
        });

        scope.change = function () {
          if (scope.assets.length > 0) {
            scope.rand = Math.floor(Math.random() * (scope.assets.length - 1)) + 1;

            if (scope.assets[scope.rand]) {
              scope.loading = true;

              scope.oldBg = element.children(':first');

              scope.newBg = angular.element('<div/>').addClass('image').addClass('fade-out');


              $imagePreload(scope.assets[scope.rand].img).then(function () {
                scope.bg = {};

                scope.newBg.css({
                  'background-image': 'url(' + scope.assets[scope.rand].img + ')' });


                element.append(scope.newBg);
                $compile(scope.newBg)(scope);
                $animate.addClass(scope.oldBg, 'fade-out');

                $timeout(function () {
                  scope.bg.img = scope.assets[scope.rand].img;
                  scope.bg.title = scope.assets[scope.rand].title;
                  scope.bg.author = scope.assets[scope.rand].author;
                  scope.bg.authorLink = scope.assets[scope.rand].author; // 'https://www.reddit.com/u/'
                  scope.bg.link = scope.assets[scope.rand].link; // 'https://www.reddit.com'
                  scope.bg.subreddit = '/r/' + scope.assets[scope.rand].subreddit;
                  scope.bg.show = true;
                }, 1000);

                $animate.removeClass(scope.newBg, 'fade-out').then(function () {
                  $timeout(function () {
                    scope.oldBg.remove();
                  }, 5000);
                });

              });

              scope.loading = false;

            }
          } else {
            scope.stopChange();
          }
        };

        scope.startChange = function () {
          if (angular.isDefined(scope.bgProcess)) {
            return;
          }

          scope.bgProcess = $interval(function () {
            scope.change();
          }, 25000);
        };

        scope.stopChange = function () {
          if (angular.isDefined(scope.bgProcess)) {
            $interval.cancel(scope.bgProcess);
            scope.bgProcess = undefined;
          }
        };

        element.on('$destroy', function () {
          $interval.cancel(scope.bgProcess);
        });

        $http(scope.config).
        success(function (response) {
          scope.data = response.data.children;

          angular.forEach(scope.data, function (value) {
            if (value.data.preview && value.data.preview.images[0].source.url && scope.height < value.data.preview.images[0].source.height && scope.width < value.data.preview.images[0].source.width) {
              // $log.debug('value.data', value.data);

              this.push({
                author: value.data.author,
                link: value.data.permalink,
                title: value.data.title,
                subreddit: value.data.subreddit,
                img: value.data.preview.images[0].source.url.replace(/^http:\/\//i, 'https://') });


              if (element.children(':first') && !element.children(':first').css('background-image')) {
                scope.change();
              }
            }
          }, scope.assets);

          if (scope.auto) {
            scope.startChange();
          }

        }, function (response) {
          // $log.error(response);
        });

      } };

  }]);

})(window.angular);
//# sourceURL=pen.js
</script>
</body></html>
