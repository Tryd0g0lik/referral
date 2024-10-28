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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _services_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./services/coockieSessionId */ \"./src/scripts/services/coockieSessionId.ts\");\n/* harmony import */ var _services_fetches__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./services/fetches */ \"./src/scripts/services/fetches.ts\");\n\n\ndocument.addEventListener(\"DOMContentLoaded\", () => {\n  //   /* сделать прослушку для к \"#submit-repeat\". Через \"fetch\"\n  //   запросить \"/repeat_token\" и все. Даьше заработает код python из\n  //   \"referral/views_more/views_account.py\"\n  //   */\n  // sessionStorage.clear()\n  // const cookie = checkCookieExists('user_token')\n  // console.log(`Hallo world!: ${cookie}`) /token/get\n  (0,_services_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.checkCookie)();\n  const href_arr = location.href.split('data_number=');\n  if (href_arr.length <= 1) {\n    return false;\n  }\n  const dataNumberStr = href_arr[1];\n  if (!dataNumberStr && !Number(dataNumberStr)) {}\n  // setCookie('user_token, ')\n  async function TestCookieFunction() {\n    const body_ = JSON.stringify({\n      userId: String(dataNumberStr)\n    });\n    const responce = await (0,_services_fetches__WEBPACK_IMPORTED_MODULE_1__.add)(body_, `/api/v1/token/get`);\n    console.log(`[POSR]: ${responce}`);\n  }\n  TestCookieFunction();\n  // console.log(\"ddddddddd\" + dataNumberStr)\n});\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/listener.ts?");

/***/ }),

/***/ "./src/scripts/services/coockieSessionId.ts":
/*!**************************************************!*\
  !*** ./src/scripts/services/coockieSessionId.ts ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   checkCookie: () => (/* binding */ checkCookie),\n/* harmony export */   checkCookieExists: () => (/* binding */ checkCookieExists),\n/* harmony export */   checkerCookieKey: () => (/* binding */ checkerCookieKey),\n/* harmony export */   createSessionId: () => (/* binding */ createSessionId),\n/* harmony export */   deleteCookie: () => (/* binding */ deleteCookie),\n/* harmony export */   getCookie: () => (/* binding */ getCookie),\n/* harmony export */   getMetasCookie: () => (/* binding */ getMetasCookie),\n/* harmony export */   setCookie: () => (/* binding */ setCookie),\n/* harmony export */   setSessionIdInCookie: () => (/* binding */ setSessionIdInCookie)\n/* harmony export */ });\n/* harmony import */ var uuid__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! uuid */ \"./node_modules/uuid/dist/esm-browser/v4.js\");\nfunction ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }\nfunction _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }\nfunction _defineProperty(e, r, t) { return (r = _toPropertyKey(r)) in e ? Object.defineProperty(e, r, { value: t, enumerable: !0, configurable: !0, writable: !0 }) : e[r] = t, e; }\nfunction _toPropertyKey(t) { var i = _toPrimitive(t, \"string\"); return \"symbol\" == typeof i ? i : i + \"\"; }\nfunction _toPrimitive(t, r) { if (\"object\" != typeof t || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || \"default\"); if (\"object\" != typeof i) return i; throw new TypeError(\"@@toPrimitive must return a primitive value.\"); } return (\"string\" === r ? String : Number)(t); }\n\nconst env = \"MISSING_ENV_VAR\".REACT_APP_POSTGRES_HOST;\nconst REACT_APP_POSTGRES_HOST = env ? env : \"localhost\";\n/**\n *\n * @param sessionId that is install the key 'sessionId'\n */\nfunction setSessionIdInCookie(sessionId) {\n  const cookieName = 'sessionId';\n  const cookieValue = sessionId;\n  const maxAge = 60 * 60 * 24; // Время жизни cookie в секундах (например, 1 день)\n\n  let now = new Date();\n  const options = {\n    expires: String(maxAge - now.getTime()),\n    path: '/',\n    domain: REACT_APP_POSTGRES_HOST,\n    secure: false,\n    sameSite: 'Strict'\n  };\n  setCookie(cookieName, cookieValue, options);\n}\n\n/**\n *\n * @param cookieName entrypoint received the a key-name from cookie and check his.\n * @returns trye/false;\n */\nfunction checkCookieExists(cookieName) {\n  // Получаем все cookies в виде строки\n  const cookies = document.cookie;\n\n  // Создаем регулярное выражение для поиска конкретного ключа\n  const regex = new RegExp('(^|; )' + encodeURIComponent(cookieName) + '=([^;]*)');\n\n  // Проверяем, есть ли совпадение\n  return regex.test(cookies);\n}\nfunction checkCookie() {\n  /**\n   * This function is an init checker. It check the status cookie - It work is or not.\n   */\n  document.cookie = \"ex=1;\";\n  if (!document.cookie) {\n    alert(\"Включите cookie для корректной работы!\");\n  }\n}\n\n// Пример использования\n// setSessionIdInCookie('abc123');\n// Генерируем уникальный идентификатор\nfunction createSessionId() {\n  return (0,uuid__WEBPACK_IMPORTED_MODULE_0__[\"default\"])();\n}\n\n/**\n * Если видим ключа 'sessionId' - cookie ,\n * Смотрим класс 'active'.\n * Если нету, добавляем.\n *\n * Если не видим ключа 'sessionId' - cookie ,\n   Смотрим класс 'active' и удаляем его.\n * @returns\n */\nasync function checkerCookieKey() {\n  const trueFalse = checkCookieExists('sessionId');\n  const root = document.getElementById('root');\n  if (root === null) {\n    return false;\n  }\n  if (trueFalse) {\n    // если видим ключ 'sessionId' - cookie ,\n    // смотрим класс 'active'.\n    // Если нету, добавляем.\n    if (!root.className.includes('active')) {\n      if (root.className.length === 0) {\n        root.className = 'active';\n      }\n      root.className = `${root.className} active`;\n    }\n  } else {\n    // если не видим ключа 'sessionId' - cookie ,\n    // смотрим класс 'active' и удаляем его.\n    if (root.className.includes('active')) {\n      root.className = root.className.replace('active', '');\n    }\n  }\n  return true;\n}\n\n/**\n * cookie Installing\n */\nfunction setCookie(name, value) {\n  let options = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : {};\n  options = _objectSpread({\n    path: '/'\n  }, options);\n  if (options.expires instanceof Date) {\n    options.expires = options.expires.toUTCString();\n  }\n\n  // Кодируем имя и значение cookie\n  let updatedCookie = encodeURIComponent(name) + \"=\" + encodeURIComponent(value);\n  for (const optionKey in options) {\n    updatedCookie += \"; \" + optionKey;\n    const optionValue = options[optionKey];\n    if (optionValue !== true) {\n      updatedCookie += \"=\" + optionValue;\n    }\n  }\n  //  \"sessionId=f835abe5-2cd4-4dd4-b797-b3da92ffd005; path=/; expires=1723938402215; domain=localhost; secure=false; sameSite=Strict\"\n\n  document.cookie = updatedCookie;\n}\n\n/**\n * Searcher for cookie's key\n * @param name\n * @returns\n */\nfunction getCookie(name) {\n  // eslint-disable-next-line\n  // let matches = document.cookie.match(new RegExp(\"(?:^|; )\" + name.replace(/([\\.$?*|{}\\(\\)\\[\\]\\\\\\/\\+^])/g, '\\\\$1') + \"=([^;]*)\"));\n  // let csrftoken = matches ? decodeURIComponent(matches[1]) : undefined;\n\n  // return csrftoken\n  // const value = `${document.cookie}`;\n  // const parts = value.split(`${name}=`);\n\n  // if (parts && parts.length === 2) {\n  //   return ((parts as Array<string>).pop() as string).split(';').shift();\n  // }\n  let cookieValue = null;\n  if (document.cookie !== undefined && document.cookie !== '') {\n    const cookies = document.cookie.split(';');\n    for (let i = 0; i < cookies.length; i++) {\n      const cookie = cookies[i].trim();\n      // Does this cookie string begin with the name we want?\n      if (cookie.substring(0, name.length + 1) === name + '=') {\n        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));\n        break;\n      }\n    }\n  }\n  return cookieValue;\n}\nfunction getMetasCookie() {\n  const csrfToken = document.querySelector('meta[name=\"csrf-token\"]');\n  if (!csrfToken) {\n    return \"\";\n  }\n  return csrfToken.getAttribute('content');\n}\nfunction deleteCookie(cookieName) {\n  document.cookie = `${cookieName}=; Max-Age=0; path=/;`;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/coockieSessionId.ts?");

/***/ }),

/***/ "./src/scripts/services/fetches.ts":
/*!*****************************************!*\
  !*** ./src/scripts/services/fetches.ts ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   add: () => (/* binding */ add),\n/* harmony export */   get: () => (/* binding */ get)\n/* harmony export */ });\n/* harmony import */ var _Interfaces__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @Interfaces */ \"./src/interfaces.ts\");\n/* harmony import */ var src_dotenv___WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/dotenv_ */ \"./src/dotenv_.ts\");\n\n\nconst params = {\n  method: _Interfaces__WEBPACK_IMPORTED_MODULE_0__.FetchMethod.POST\n};\n\n/**\n *\n * @param body_ Here is data for db + \\ 'X-CSRFToken': getCookie('csrftoken') as string,\n * sessionId ` {\n    sessionId: cookieId\n  };`. //\n * @param pathnameStr '/it/is/api/path/'\n * @returns JSON of boolesn\n */\nasync function add(body_) {\n  let pathnameStr = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : '/api/v1/referral/add';\n  let response = await get(`/csrf_token`);\n  let csrf_token = \"\";\n  if (response[\"csrf_token\"]) {\n    csrf_token += response[\"csrf_token\"];\n  }\n\n  // params[\"credentials\"] = 'include',\n  params['headers'] = {\n    'X-CSRFToken': csrf_token,\n    // getMetasCookie() as string,// getCookie('csrftoken') as string, // csrftoken\n    'Content-Type': 'application/json'\n  };\n  params['body'] = body_;\n  const paramsCopy = {};\n  Object.assign(paramsCopy, params);\n  const urlStr = `${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PROTOCOL}://${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_HOST}:${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PORT}`;\n  const url = urlStr + pathnameStr;\n  const answer = await fetch(url, paramsCopy);\n  if (answer.ok) {\n    const response = await answer.json();\n    return response;\n  }\n  return false;\n}\nasync function get() {\n  let pathnameStr = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '/api/v1/clients/add/';\n  const urlStr = `${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PROTOCOL}://${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_HOST}:${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PORT}`;\n  const url = urlStr + pathnameStr;\n  const answer = await fetch(url, {\n    method: 'GET',\n    headers: {\n      'Content-Type': 'application/json'\n    }\n  });\n  if (answer.ok) {\n    const dataJson = await answer.json();\n    return dataJson;\n  }\n  return false;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/fetches.ts?");

/***/ }),

/***/ "./src/styles/style.css":
/*!******************************!*\
  !*** ./src/styles/style.css ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack://frontend-Flask-account/./src/styles/style.css?");

/***/ }),

/***/ "./node_modules/uuid/dist/esm-browser/regex.js":
/*!*****************************************************!*\
  !*** ./node_modules/uuid/dist/esm-browser/regex.js ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (/^(?:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}|00000000-0000-0000-0000-000000000000)$/i);\n\n//# sourceURL=webpack://frontend-Flask-account/./node_modules/uuid/dist/esm-browser/regex.js?");

/***/ }),

/***/ "./node_modules/uuid/dist/esm-browser/rng.js":
/*!***************************************************!*\
  !*** ./node_modules/uuid/dist/esm-browser/rng.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ rng)\n/* harmony export */ });\n// Unique ID creation requires a high quality random # generator. In the browser we therefore\n// require the crypto API and do not support built-in fallback to lower quality random number\n// generators (like Math.random()).\nvar getRandomValues;\nvar rnds8 = new Uint8Array(16);\nfunction rng() {\n  // lazy load so that environments that need to polyfill have a chance to do so\n  if (!getRandomValues) {\n    // getRandomValues needs to be invoked in a context where \"this\" is a Crypto implementation. Also,\n    // find the complete implementation of crypto (msCrypto) on IE11.\n    getRandomValues = typeof crypto !== 'undefined' && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || typeof msCrypto !== 'undefined' && typeof msCrypto.getRandomValues === 'function' && msCrypto.getRandomValues.bind(msCrypto);\n\n    if (!getRandomValues) {\n      throw new Error('crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported');\n    }\n  }\n\n  return getRandomValues(rnds8);\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./node_modules/uuid/dist/esm-browser/rng.js?");

/***/ }),

/***/ "./node_modules/uuid/dist/esm-browser/stringify.js":
/*!*********************************************************!*\
  !*** ./node_modules/uuid/dist/esm-browser/stringify.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var _validate_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./validate.js */ \"./node_modules/uuid/dist/esm-browser/validate.js\");\n\n/**\n * Convert array of 16 byte values to UUID string format of the form:\n * XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX\n */\n\nvar byteToHex = [];\n\nfor (var i = 0; i < 256; ++i) {\n  byteToHex.push((i + 0x100).toString(16).substr(1));\n}\n\nfunction stringify(arr) {\n  var offset = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 0;\n  // Note: Be careful editing this code!  It's been tuned for performance\n  // and works in ways you may not expect. See https://github.com/uuidjs/uuid/pull/434\n  var uuid = (byteToHex[arr[offset + 0]] + byteToHex[arr[offset + 1]] + byteToHex[arr[offset + 2]] + byteToHex[arr[offset + 3]] + '-' + byteToHex[arr[offset + 4]] + byteToHex[arr[offset + 5]] + '-' + byteToHex[arr[offset + 6]] + byteToHex[arr[offset + 7]] + '-' + byteToHex[arr[offset + 8]] + byteToHex[arr[offset + 9]] + '-' + byteToHex[arr[offset + 10]] + byteToHex[arr[offset + 11]] + byteToHex[arr[offset + 12]] + byteToHex[arr[offset + 13]] + byteToHex[arr[offset + 14]] + byteToHex[arr[offset + 15]]).toLowerCase(); // Consistency check for valid UUID.  If this throws, it's likely due to one\n  // of the following:\n  // - One or more input array values don't map to a hex octet (leading to\n  // \"undefined\" in the uuid)\n  // - Invalid input values for the RFC `version` or `variant` fields\n\n  if (!(0,_validate_js__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(uuid)) {\n    throw TypeError('Stringified UUID is invalid');\n  }\n\n  return uuid;\n}\n\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (stringify);\n\n//# sourceURL=webpack://frontend-Flask-account/./node_modules/uuid/dist/esm-browser/stringify.js?");

/***/ }),

/***/ "./node_modules/uuid/dist/esm-browser/v4.js":
/*!**************************************************!*\
  !*** ./node_modules/uuid/dist/esm-browser/v4.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var _rng_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./rng.js */ \"./node_modules/uuid/dist/esm-browser/rng.js\");\n/* harmony import */ var _stringify_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./stringify.js */ \"./node_modules/uuid/dist/esm-browser/stringify.js\");\n\n\n\nfunction v4(options, buf, offset) {\n  options = options || {};\n  var rnds = options.random || (options.rng || _rng_js__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(); // Per 4.4, set bits for version and `clock_seq_hi_and_reserved`\n\n  rnds[6] = rnds[6] & 0x0f | 0x40;\n  rnds[8] = rnds[8] & 0x3f | 0x80; // Copy bytes to buffer, if provided\n\n  if (buf) {\n    offset = offset || 0;\n\n    for (var i = 0; i < 16; ++i) {\n      buf[offset + i] = rnds[i];\n    }\n\n    return buf;\n  }\n\n  return (0,_stringify_js__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(rnds);\n}\n\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (v4);\n\n//# sourceURL=webpack://frontend-Flask-account/./node_modules/uuid/dist/esm-browser/v4.js?");

/***/ }),

/***/ "./node_modules/uuid/dist/esm-browser/validate.js":
/*!********************************************************!*\
  !*** ./node_modules/uuid/dist/esm-browser/validate.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var _regex_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./regex.js */ \"./node_modules/uuid/dist/esm-browser/regex.js\");\n\n\nfunction validate(uuid) {\n  return typeof uuid === 'string' && _regex_js__WEBPACK_IMPORTED_MODULE_0__[\"default\"].test(uuid);\n}\n\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (validate);\n\n//# sourceURL=webpack://frontend-Flask-account/./node_modules/uuid/dist/esm-browser/validate.js?");

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
