/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./src/dotenv_.ts":
/*!************************!*\
  !*** ./src/dotenv_.ts ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   PROJECT_REFERRAL_HOST: () => (/* binding */ PROJECT_REFERRAL_HOST),\n/* harmony export */   PROJECT_REFERRAL_PORT: () => (/* binding */ PROJECT_REFERRAL_PORT),\n/* harmony export */   PROJECT_REFERRAL_PROTOCOL: () => (/* binding */ PROJECT_REFERRAL_PROTOCOL)\n/* harmony export */ });\nlet env_ = \"localhost\";\nconst PROJECT_REFERRAL_HOST = env_ === undefined ? \"localhost\" : env_.slice(0);\nenv_ = \"5000\";\nconst PROJECT_REFERRAL_PORT = env_ === undefined ? \"localhost\" : env_.slice(0);\nenv_ = \"http\";\nconst PROJECT_REFERRAL_PROTOCOL = env_ === undefined ? \"loocalhost\" : env_.slice(0);\n\n//# sourceURL=webpack://frontend-Flask-account/./src/dotenv_.ts?");

/***/ }),

/***/ "./src/index.ts":
/*!**********************!*\
  !*** ./src/index.ts ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _styles_style_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./styles/style.css */ \"./src/styles/style.css\");\n/* harmony import */ var _scripts_listener_ts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./scripts/listener.ts */ \"./src/scripts/listener.ts\");\n\n\nconsole.log(\"Hallo world!\");\n\n//# sourceURL=webpack://frontend-Flask-account/./src/index.ts?");

/***/ }),

/***/ "./src/interfaces.ts":
/*!***************************!*\
  !*** ./src/interfaces.ts ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   FetchMethod: () => (/* binding */ FetchMethod)\n/* harmony export */ });\nlet FetchMethod = /*#__PURE__*/function (FetchMethod) {\n  FetchMethod[\"POST\"] = \"POST\";\n  FetchMethod[\"GET\"] = \"GET\";\n  FetchMethod[\"PUT\"] = \"PUT\";\n  FetchMethod[\"PATCH\"] = \"PATCH\";\n  FetchMethod[\"DELETE\"] = \"DELETE\";\n  return FetchMethod;\n}({});\n\n//# sourceURL=webpack://frontend-Flask-account/./src/interfaces.ts?");

/***/ }),

/***/ "./src/scripts/listener.ts":
/*!*********************************!*\
  !*** ./src/scripts/listener.ts ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _services_fetches__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./services/fetches */ \"./src/scripts/services/fetches.ts\");\n\ndocument.addEventListener(\"DOMContentLoaded\", () => {\n  //   /* сделать прослушку для к \"#submit-repeat\". Через \"fetch\"\n  //   запросить \"/repeat_token\" и все. Даьше заработает код python из\n  //   \"referral/views_more/views_account.py\"\n  //   */\n  // sessionStorage.clear()\n  // const cookie = checkCookieExists('user_token')\n  // console.log(`Hallo world!: ${cookie}`) /token/get\n  const cookie_arr = location.href.split('data_number=');\n  if (cookie_arr.length <= 1) {\n    return false;\n  }\n  const dataNumberStr = cookie_arr[1];\n  if (dataNumberStr && Number(dataNumberStr)) {\n    const body_ = {\n      data_number: Number(dataNumberStr)\n    };\n    (0,_services_fetches__WEBPACK_IMPORTED_MODULE_0__.add)(JSON.stringify(body_), \"/api/v1/token/get\");\n  }\n  // setCookie('user_token, ')\n\n  console.log(\"ddddddddd\" + dataNumberStr);\n});\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/listener.ts?");

/***/ }),

/***/ "./src/scripts/services/fetches.ts":
/*!*****************************************!*\
  !*** ./src/scripts/services/fetches.ts ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   add: () => (/* binding */ add)\n/* harmony export */ });\n/* harmony import */ var _Interfaces__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @Interfaces */ \"./src/interfaces.ts\");\n/* harmony import */ var src_dotenv___WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/dotenv_ */ \"./src/dotenv_.ts\");\n\n// import { getCookie } from \"./coockieSessionId\";\n\nconst params = {\n  method: _Interfaces__WEBPACK_IMPORTED_MODULE_0__.FetchMethod.POST,\n  mode: 'cors'\n};\n\n/**\n *\n * @param body_ Here is data for db + \\ 'X-CSRFToken': getCookie('csrftoken') as string,\n * sessionId ` {\n    sessionId: cookieId\n  };`.\n * @param pathnameStr '/it/is/api/path/'\n * @returns JSON of boolesn\n */\nasync function add(body_) {\n  let pathnameStr = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : '/api/v1/referral/add/';\n  params['headers'] = {\n    'Content-Type': 'application/json'\n  };\n  params['body'] = body_;\n  const paramsCopy = {};\n  Object.assign(paramsCopy, params);\n  const urlStr = `${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PROTOCOL}://${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_HOST}:${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PORT}`;\n  const url = urlStr + pathnameStr;\n  const answer = await fetch(url, paramsCopy);\n  if (answer.ok) {\n    const dataJson = answer.json();\n    return dataJson;\n  }\n  return false;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/fetches.ts?");

/***/ }),

/***/ "./src/styles/style.css":
/*!******************************!*\
  !*** ./src/styles/style.css ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack://frontend-Flask-account/./src/styles/style.css?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./src/index.ts");
/******/ 	
/******/ })()
;