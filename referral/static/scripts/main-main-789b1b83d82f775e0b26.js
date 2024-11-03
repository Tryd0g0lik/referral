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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _styles_style_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./styles/style.css */ \"./src/styles/style.css\");\n/* harmony import */ var _scripts_index_ts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./scripts/index.ts */ \"./src/scripts/index.ts\");\n/* harmony import */ var _scripts_listener_ts__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./scripts/listener.ts */ \"./src/scripts/listener.ts\");\n\n\n\nconsole.log(\"Hallo world!\");\n\n//# sourceURL=webpack://frontend-Flask-account/./src/index.ts?");

/***/ }),

/***/ "./src/interfaces.ts":
/*!***************************!*\
  !*** ./src/interfaces.ts ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   FetchMethod: () => (/* binding */ FetchMethod)\n/* harmony export */ });\nlet FetchMethod = /*#__PURE__*/function (FetchMethod) {\n  FetchMethod[\"POST\"] = \"POST\";\n  FetchMethod[\"GET\"] = \"GET\";\n  FetchMethod[\"PUT\"] = \"PUT\";\n  FetchMethod[\"PATCH\"] = \"PATCH\";\n  FetchMethod[\"DELETE\"] = \"DELETE\";\n  return FetchMethod;\n}({});\n\n//# sourceURL=webpack://frontend-Flask-account/./src/interfaces.ts?");

/***/ }),

/***/ "./src/scripts/index.ts":
/*!******************************!*\
  !*** ./src/scripts/index.ts ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _services_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./services/coockieSessionId */ \"./src/scripts/services/coockieSessionId.ts\");\n/* harmony import */ var _services_tokens__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./services/tokens */ \"./src/scripts/services/tokens.ts\");\nfunction ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }\nfunction _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }\nfunction _defineProperty(e, r, t) { return (r = _toPropertyKey(r)) in e ? Object.defineProperty(e, r, { value: t, enumerable: !0, configurable: !0, writable: !0 }) : e[r] = t, e; }\nfunction _toPropertyKey(t) { var i = _toPrimitive(t, \"string\"); return \"symbol\" == typeof i ? i : i + \"\"; }\nfunction _toPrimitive(t, r) { if (\"object\" != typeof t || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || \"default\"); if (\"object\" != typeof i) return i; throw new TypeError(\"@@toPrimitive must return a primitive value.\"); } return (\"string\" === r ? String : Number)(t); }\n\n\n/** This is  a main page (start). */\ndocument.addEventListener(\"DOMContentLoaded\", () => {\n  /*\n   * Chack a cookie. It works or not.\n   * If has not work cookie, get the alert to display.\n   */\n  (0,_services_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.checkCookie)();\n  /**\n   * From the URL-address receive the 'data_number'. It is \\\n   * data from backend.\n   */\n  const href_arr = location.href.split('data_number=');\n  if (href_arr.length <= 1) {\n    return false;\n  }\n  const dataNumberStr = href_arr[1];\n  if (!dataNumberStr && !Number(dataNumberStr)) {}\n\n  // Primary installation the user roken/\n  initUserToken(dataNumberStr);\n});\nasync function initUserToken(dataNumberStr) {\n  /**\n   * @param dataNumberStr: string. This is a user id fron the URL.\n   */\n  // Here, user-token is receive from the db.\n  const userTokenObj = await (0,_services_tokens__WEBPACK_IMPORTED_MODULE_1__.getUserToken)(dataNumberStr);\n  if (!(typeof userTokenObj).includes(\"object\")) {\n    console.warn(\"[initUserToken]: Not received user's token\");\n    return false;\n  }\n  if (!userTokenObj || !(typeof userTokenObj).includes('object') || (typeof userTokenObj).includes('object') && !userTokenObj[\"user_token\"]) {\n    console.warn(\"[initUserToken]: Not received a variable 'user_token' from backend\");\n    return false;\n  }\n  // To keep user-token in the Cookie\n  (0,_services_tokens__WEBPACK_IMPORTED_MODULE_1__.setUserToken)(_objectSpread({}, userTokenObj));\n  return true;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/index.ts?");

/***/ }),

/***/ "./src/scripts/listener.ts":
/*!*********************************!*\
  !*** ./src/scripts/listener.ts ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _services_handlers_handlerPageLoade__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./services/handlers/handlerPageLoade */ \"./src/scripts/services/handlers/handlerPageLoade.ts\");\n/* harmony import */ var _services_handlers_handlerReferrals__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./services/handlers/handlerReferrals */ \"./src/scripts/services/handlers/handlerReferrals.ts\");\n/* harmony import */ var _services_handlers_handlerRemoveProfile__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./services/handlers/handlerRemoveProfile */ \"./src/scripts/services/handlers/handlerRemoveProfile.ts\");\n/* harmony import */ var _services_handlers_handlerTokenRepeats__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./services/handlers/handlerTokenRepeats */ \"./src/scripts/services/handlers/handlerTokenRepeats.ts\");\n/* harmony import */ var _services_handlers_subFunctions__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./services/handlers/subFunctions */ \"./src/scripts/services/handlers/subFunctions.ts\");\n/** This is  a collection of event's listaner .*/\n\n\n\n\n\ndocument.addEventListener(\"DOMContentLoaded\", e => {\n  /*  Referral code */\n  const formHtml = document.querySelector('#referral');\n  if (formHtml !== null) {\n    formHtml.removeEventListener(\"mousedown\", _services_handlers_handlerReferrals__WEBPACK_IMPORTED_MODULE_1__.handlerAddReferral);\n    formHtml.addEventListener(\"mousedown\", _services_handlers_handlerReferrals__WEBPACK_IMPORTED_MODULE_1__.handlerAddReferral);\n    formHtml.removeEventListener(\"keydown\", _services_handlers_handlerReferrals__WEBPACK_IMPORTED_MODULE_1__.handlerAddReferral);\n    formHtml.addEventListener(\"keydown\", _services_handlers_handlerReferrals__WEBPACK_IMPORTED_MODULE_1__.handlerAddReferral);\n  } else {\n    console.warn(\"[listener]: Not found '#referral'. \");\n  }\n  /* Page for a repeat link for authentication. */\n  const mainHtml = document.querySelector('main');\n  if (location.pathname.includes('/repeat_token')) {\n    mainHtml.removeEventListener(\"click\", _services_handlers_handlerTokenRepeats__WEBPACK_IMPORTED_MODULE_3__.handlerTokenRepeat);\n  } else if (location.href.includes(\"/profile/delete\")) {\n    // Profile is delete\n    const inputHTML = document.querySelector(\"#removing\");\n    if (inputHTML === null) {\n      console.warn(\"[listener] Form was not found for the profile removing!\");\n      return false;\n    }\n    inputHTML.removeEventListener(\"submit\", _services_handlers_handlerRemoveProfile__WEBPACK_IMPORTED_MODULE_2__.handlerProfileRemove);\n    inputHTML.addEventListener(\"submit\", _services_handlers_handlerRemoveProfile__WEBPACK_IMPORTED_MODULE_2__.handlerProfileRemove);\n  } else if (location.href.includes(\"/profile\")) {\n    // Loade page and referral publication\n    (0,_services_handlers_handlerPageLoade__WEBPACK_IMPORTED_MODULE_0__.handlerLoderPage)();\n    /*\n     Profile is delete.\n     Function timeOut works with 'setTimeout'.\n    */\n    (0,_services_handlers_subFunctions__WEBPACK_IMPORTED_MODULE_4__.timeOut)(10);\n  } else if (mainHtml !== null && !location.pathname.includes('/repeat_token')) {\n    mainHtml.removeEventListener(\"click\", _services_handlers_handlerTokenRepeats__WEBPACK_IMPORTED_MODULE_3__.handlerTokenRepeat);\n    mainHtml.addEventListener(\"click\", _services_handlers_handlerTokenRepeats__WEBPACK_IMPORTED_MODULE_3__.handlerTokenRepeat);\n  } else {\n    console.warn(\"[listener]: Not found '#submit-repeat'. \");\n  }\n});\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/listener.ts?");

/***/ }),

/***/ "./src/scripts/services/coockieSessionId.ts":
/*!**************************************************!*\
  !*** ./src/scripts/services/coockieSessionId.ts ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   checkCookie: () => (/* binding */ checkCookie),\n/* harmony export */   checkCookieExists: () => (/* binding */ checkCookieExists),\n/* harmony export */   checkerCookieKey: () => (/* binding */ checkerCookieKey),\n/* harmony export */   createSessionId: () => (/* binding */ createSessionId),\n/* harmony export */   deleteCookie: () => (/* binding */ deleteCookie),\n/* harmony export */   getCookie: () => (/* binding */ getCookie),\n/* harmony export */   getMetasCookie: () => (/* binding */ getMetasCookie),\n/* harmony export */   setCookie: () => (/* binding */ setCookie),\n/* harmony export */   setSessionIdInCookie: () => (/* binding */ setSessionIdInCookie)\n/* harmony export */ });\n/* harmony import */ var uuid__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! uuid */ \"./node_modules/uuid/dist/esm-browser/v4.js\");\nfunction ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }\nfunction _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }\nfunction _defineProperty(e, r, t) { return (r = _toPropertyKey(r)) in e ? Object.defineProperty(e, r, { value: t, enumerable: !0, configurable: !0, writable: !0 }) : e[r] = t, e; }\nfunction _toPropertyKey(t) { var i = _toPrimitive(t, \"string\"); return \"symbol\" == typeof i ? i : i + \"\"; }\nfunction _toPrimitive(t, r) { if (\"object\" != typeof t || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || \"default\"); if (\"object\" != typeof i) return i; throw new TypeError(\"@@toPrimitive must return a primitive value.\"); } return (\"string\" === r ? String : Number)(t); }\n\nconst env = \"MISSING_ENV_VAR\".REACT_APP_POSTGRES_HOST;\nconst REACT_APP_POSTGRES_HOST = env ? env : \"localhost\";\n/**\n *\n * @param sessionId that is install the key 'sessionId'\n */\nfunction setSessionIdInCookie(sessionId) {\n  const cookieName = 'sessionId';\n  const cookieValue = sessionId;\n  const maxAge = 60 * 60 * 24; // Время жизни cookie в секундах (например, 1 день)\n\n  let now = new Date();\n  const options = {\n    expires: String(maxAge - now.getTime()),\n    path: '/',\n    domain: REACT_APP_POSTGRES_HOST,\n    secure: false,\n    sameSite: 'Strict'\n  };\n  setCookie(cookieName, cookieValue, options);\n}\n\n/**\n *\n * @param cookieName entrypoint received the a key-name from cookie and check his.\n * @returns trye/false;\n */\nfunction checkCookieExists(cookieName) {\n  // Получаем все cookies в виде строки\n  const cookies = document.cookie;\n\n  // Создаем регулярное выражение для поиска конкретного ключа\n  const regex = new RegExp('(^|; )' + encodeURIComponent(cookieName) + '=([^;]*)');\n\n  // Проверяем, есть ли совпадение\n  return regex.test(cookies);\n}\nfunction checkCookie() {\n  /**\n   * This function is an init checker. It check the status cookie - It work is or not.\n   */\n  document.cookie = \"ex=1;\";\n  if (!document.cookie) {\n    alert(\"Включите cookie для корректной работы!\");\n  }\n}\n\n// Генерируем уникальный идентификатор\nfunction createSessionId() {\n  return (0,uuid__WEBPACK_IMPORTED_MODULE_0__[\"default\"])();\n}\n\n/**\n * Если видим ключа 'sessionId' - cookie ,\n * Смотрим класс 'active'.\n * Если нету, добавляем.\n *\n * Если не видим ключа 'sessionId' - cookie ,\n   Смотрим класс 'active' и удаляем его.\n * @returns\n */\nasync function checkerCookieKey(name) {\n  const trueFalse = checkCookieExists(name);\n  const root = document.getElementById('root');\n  if (root === null) {\n    return false;\n  }\n  if (trueFalse) {\n    // если видим ключ 'sessionId' - cookie ,\n    // смотрим класс 'active'.\n    // Если нету, добавляем.\n    if (!root.className.includes('active')) {\n      if (root.className.length === 0) {\n        root.className = 'active';\n      }\n      root.className = `${root.className} active`;\n    }\n  } else {\n    // если не видим ключа 'sessionId' - cookie ,\n    // смотрим класс 'active' и удаляем его.\n    if (root.className.includes('active')) {\n      root.className = root.className.replace('active', '');\n    }\n  }\n  return true;\n}\n\n/**\n   * Keep data to the cookie.\n   * Exemple result:\n   *  \"sessionId=f835abe5-2cd4-4dd4-b797-b3da92ffd005; path=/; expires=1723938402215; domain=localhost; secure=false; sameSite=Strict\"\n   * @param name: string. This is a name of key for cookie.\n   * @param value: string  This is a value for key from the cookie.\n   * @param options: object of type 'CookieOptions'.\n    ```ts\n      interface CookieOptions {\n        expires?: Date | string;\n        path?: string;\n        domain?: string;\n        secure?: boolean;\n        sameSite?: 'Strict' | 'Lax' | 'None';\n      }\n    ```\n   */\nfunction setCookie(name, value) {\n  let options = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : {};\n  options = _objectSpread({\n    path: '/'\n  }, options);\n  if (options.expires instanceof Date) {\n    options.expires = options.expires.toUTCString();\n  }\n\n  // Кодируем имя и значение cookie\n  let updatedCookie = encodeURIComponent(name) + \"=\" + encodeURIComponent(value);\n  for (const optionKey in options) {\n    updatedCookie += \"; \" + optionKey;\n    const optionValue = options[optionKey];\n    if (optionValue !== true) {\n      updatedCookie += \"=\" + optionValue;\n    }\n  }\n  document.cookie = updatedCookie;\n}\n\n/**\n * Searcher for cookie's key\n * @param name\n * @returns\n */\nfunction getCookie(name) {\n  // eslint-disable-next-line\n  // let matches = document.cookie.match(new RegExp(\"(?:^|; )\" + name.replace(/([\\.$?*|{}\\(\\)\\[\\]\\\\\\/\\+^])/g, '\\\\$1') + \"=([^;]*)\"));\n  // let csrftoken = matches ? decodeURIComponent(matches[1]) : undefined;\n\n  // return csrftoken\n  // const value = `${document.cookie}`;\n  // const parts = value.split(`${name}=`);\n\n  // if (parts && parts.length === 2) {\n  //   return ((parts as Array<string>).pop() as string).split(';').shift();\n  // }\n  let cookieValue = '';\n  if (document.cookie !== undefined && document.cookie !== '') {\n    const cookies = document.cookie.split(';');\n    for (let i = 0; i < cookies.length; i++) {\n      const cookie = cookies[i].trim();\n      // Does this cookie string begin with the name we want?\n      if (cookie.substring(0, name.length + 1) === name + '=') {\n        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));\n        break;\n      }\n    }\n  }\n  return cookieValue;\n}\nfunction getMetasCookie() {\n  const csrfToken = document.querySelector('meta[name=\"csrf-token\"]');\n  if (!csrfToken) {\n    return \"\";\n  }\n  return csrfToken.getAttribute('content');\n}\nfunction deleteCookie(cookieName) {\n  document.cookie = `${cookieName}=; Max-Age=0; path=/;`;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/coockieSessionId.ts?");

/***/ }),

/***/ "./src/scripts/services/fetches.ts":
/*!*****************************************!*\
  !*** ./src/scripts/services/fetches.ts ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   add: () => (/* binding */ add),\n/* harmony export */   get: () => (/* binding */ get)\n/* harmony export */ });\n/* harmony import */ var _Interfaces__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @Interfaces */ \"./src/interfaces.ts\");\n/* harmony import */ var src_dotenv___WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/dotenv_ */ \"./src/dotenv_.ts\");\n\n\nconst params = {\n  method: _Interfaces__WEBPACK_IMPORTED_MODULE_0__.FetchMethod.POST\n};\n\n/**\n *\n  * @param pathnameStr: string, '/it/is/api/path/'\n * @returns JSON of boolean\n */\nasync function add(body_) {\n  let pathnameStr = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : '/api/v1/referral/add';\n  /*\n   GET the csfr_token\n    - send a request 'GET' to the server.  Response receiving - 'csfr_token'.\n  */\n  let response = await get(`/csrf_token`);\n  let csrf_token = \"\";\n  if (response[\"csrf_token\"]) {\n    csrf_token += response[\"csrf_token\"];\n  }\n\n  /*\n  After, did request a 'POST' and received the 'user_token'.\n  */\n  params['headers'] = {\n    'X-CSRFToken': csrf_token,\n    'Content-Type': 'application/json'\n  };\n  params['body'] = body_;\n  const paramsCopy = {};\n  Object.assign(paramsCopy, params);\n  const urlStr = `${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PROTOCOL}://${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_HOST}:${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PORT}`;\n  const url = urlStr + pathnameStr;\n  const answer = await fetch(url, paramsCopy);\n  if (answer.ok) {\n    const response = await answer.json();\n    return response;\n  }\n  return false;\n}\nasync function get() {\n  let pathnameStr = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '/api/v1/clients/add/';\n  const urlStr = `${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PROTOCOL}://${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_HOST}:${src_dotenv___WEBPACK_IMPORTED_MODULE_1__.PROJECT_REFERRAL_PORT}`;\n  const url = urlStr + pathnameStr;\n  const answer = await fetch(url, {\n    method: 'GET',\n    headers: {\n      'Content-Type': 'application/json'\n    }\n  });\n  if (answer.ok) {\n    const dataJson = await answer.json();\n    return dataJson;\n  }\n  return false;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/fetches.ts?");

/***/ }),

/***/ "./src/scripts/services/handlers/handlerPageLoade.ts":
/*!***********************************************************!*\
  !*** ./src/scripts/services/handlers/handlerPageLoade.ts ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerLoderPage: () => (/* binding */ handlerLoderPage)\n/* harmony export */ });\n/* harmony import */ var _fetches__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../fetches */ \"./src/scripts/services/fetches.ts\");\n/* harmony import */ var _subFunctions__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./subFunctions */ \"./src/scripts/services/handlers/subFunctions.ts\");\n\n\nlet env_ = \"localhost\";\nconst HOST = env_ ? env_ : '';\nenv_ = \"5000\";\nconst PORT = env_ ? env_ : '';\nenv_ = \"http\";\nconst PROTOCOL = env_ ? env_ : '';\nasync function handlerLoderPage() {\n  let specificUrl = \"/profile\";\n  let response = (0,_subFunctions__WEBPACK_IMPORTED_MODULE_1__.getUserTokenFromProfilePage)(specificUrl);\n  if (response.length === 0) {\n    console.error(\"[handlerAddReferral]: 'userToken'  length is 0/zero !\");\n    return false;\n  }\n  const body_ = JSON.stringify({\n    userToken: response.slice(0)\n  });\n  response = await (0,_fetches__WEBPACK_IMPORTED_MODULE_0__.add)(body_, \"/api/v1/referral/get\");\n  if ((typeof response).includes(\"boolean\")) {\n    return false;\n  }\n  // publicate the referrals code\n  const reffHTML = document.querySelector(\".reff\");\n  if (reffHTML === null) {\n    return false;\n  }\n  const divHtml = document.createElement('div');\n  const bHtml = document.createElement('b');\n  const aHtml = document.createElement('a');\n  const ulHtml = document.createElement('ul');\n  bHtml.innerText = response.descript;\n  divHtml.innerHTML = bHtml.outerHTML;\n  const title = divHtml.outerHTML.slice(0);\n\n  // received a referral code\n  const referral = response.referral;\n  aHtml.href = `${PROTOCOL}://${HOST}:${PORT}/${referral}`;\n  aHtml.innerText = `${PROTOCOL}://${HOST}:${PORT}/${referral}`;\n  divHtml.innerHTML = aHtml.outerHTML;\n  const hrefHtml = divHtml.outerHTML;\n  // create a list\n  ulHtml.innerHTML = `\n  <li class=\"reff-view\">\n    ${title}\n    ${hrefHtml}\n    <div>Удалить</div>\n  </li> `;\n  reffHTML.insertAdjacentElement(\"beforeend\", ulHtml);\n\n  // publicate message from the response.\n  const p = document.createElement('p');\n  p.className = \"messages\";\n  p.innerText = response['message'];\n  const divFormMessage = document.querySelector(\".form-message\");\n  if (divFormMessage === null) {\n    return false;\n  }\n\n  // massage publicate\n  divFormMessage.innerHTML = \"\";\n  divFormMessage.replaceChildren(p.outerText);\n  return false;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/handlers/handlerPageLoade.ts?");

/***/ }),

/***/ "./src/scripts/services/handlers/handlerReferrals.ts":
/*!***********************************************************!*\
  !*** ./src/scripts/services/handlers/handlerReferrals.ts ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerAddReferral: () => (/* binding */ handlerAddReferral)\n/* harmony export */ });\n/* harmony import */ var _coockieSessionId__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../coockieSessionId */ \"./src/scripts/services/coockieSessionId.ts\");\n/* harmony import */ var _fetches__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../fetches */ \"./src/scripts/services/fetches.ts\");\n/** Handler for receive a referral code. */\n\n\nasync function handlerAddReferral(e) {\n  // Referral code.\n  // Страница с формой - для реферрал коде.\n  // Из формы на сервер уходит\n  /* {\n      userToken: response,\n      descript: < your_description > or '{Make}'\n    } */\n  if (e.type && e.type.includes(\"mousedown\") && e.target.type && e.target.type.includes(\"submit\") && e.target.id.includes(\"submit\") || e.type && e.type.includes(\"keydown\") && e.type && e.type.includes(\"keydoem\") && e.key && e.key.includes(\"Enter\")) {\n    const inputHtml = e.target;\n    if (e.key && e.key.includes(\"Enter\")) {\n      if (inputHtml === null || inputHtml.id === null || !inputHtml.id.includes(\"csrf_token\")) {\n        console.error(\"[handlerAddReferral]: Field not found! Something what wrong! \");\n        return false;\n      }\n    }\n    const p = document.createElement('p');\n    p.className = \"messages\";\n    const pHTML = document.querySelector(\"p.messages\");\n    if (pHTML !== null) {\n      pHTML.remove();\n    }\n    /* */\n    const button = document.querySelector('input#submit[type=\"submit\"]');\n    if (button === null) {\n      return false;\n    }\n    if (inputHtml.value.length === 0) {\n      p.innerText = \"Описание не ззаполненою\";\n      inputHtml.insertAdjacentElement(\"afterend\", p);\n    }\n    // Receive an user's token.\n    // Check cookie name\n    let response = (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.checkCookieExists)(\"userToken\");\n    // true or false\n    if (!response) {\n      console.error(\"[handlerAddReferral]: 'userToken' not founded from Cookie!\");\n      return false;\n    }\n    e.preventDefault();\n    button.disabled = true;\n    // Length of userToken's value.\n    response = (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.getCookie)(\"userToken\");\n    if (response.length === 0) {\n      console.error(\"[handlerAddReferral]: 'userToken'  length is 0/zero !\");\n      return false;\n    }\n    // Down, referral code adds\n    /*\n    param userToken: str from Cookie\n    param descript: description for a new refferal code\n    */\n    const body_ = JSON.stringify({\n      userToken: response,\n      descript: inputHtml.value\n    });\n    response = await (0,_fetches__WEBPACK_IMPORTED_MODULE_1__.add)(body_, \"/api/v1/referral/add\");\n    p.innerText = response['message'];\n    const formHTML = document.querySelector(\"form\");\n    if (formHTML === null) {\n      return false;\n    }\n    formHTML.insertAdjacentElement(\"afterend\", p);\n  }\n  return true;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/handlers/handlerReferrals.ts?");

/***/ }),

/***/ "./src/scripts/services/handlers/handlerReferralsRemove.ts":
/*!*****************************************************************!*\
  !*** ./src/scripts/services/handlers/handlerReferralsRemove.ts ***!
  \*****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerReferralRemovet: () => (/* binding */ handlerReferralRemovet)\n/* harmony export */ });\n/* harmony import */ var _fetches__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../fetches */ \"./src/scripts/services/fetches.ts\");\n/* harmony import */ var _subFunctions__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./subFunctions */ \"./src/scripts/services/handlers/subFunctions.ts\");\n\n\nlet env_ = \"localhost\";\nconst HOST = env_ ? env_ : '';\nenv_ = \"5000\";\nconst PORT = env_ ? env_ : '';\nenv_ = \"http\";\nconst PROTOCOL = env_ ? env_ : '';\nasync function handlerReferralRemovet(e) {\n  // PAGE\n  let specificUrl = \"/profile\";\n  let response = (0,_subFunctions__WEBPACK_IMPORTED_MODULE_1__.getUserTokenFromProfilePage)(specificUrl);\n  if (response.length === 0) {\n    console.error(\"[handlerReferralRemovet]: 'userToken'  length is 0/zero !\");\n    return false;\n  }\n\n  // CONTAINER\n  if (!e.type || !e.type.includes('mousedown') || !e.target.tagName.toLowerCase().includes('div') || !e.target.textContent || !e.target.textContent.toLowerCase()?.includes(\"удалить\")) {\n    console.error(\"[handlerReferralRemovet]: 'Удалить' was not found!\");\n    return false;\n  }\n\n  // FETCH\n  const body_ = JSON.stringify({\n    userToken: response.slice(0)\n  });\n  response = await (0,_fetches__WEBPACK_IMPORTED_MODULE_0__.add)(body_, \"/api/v1/profile/referral/delete\");\n  if ((typeof response).includes(\"boolean\")) {\n    return false;\n  }\n  return response;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/handlers/handlerReferralsRemove.ts?");

/***/ }),

/***/ "./src/scripts/services/handlers/handlerRemoveProfile.ts":
/*!***************************************************************!*\
  !*** ./src/scripts/services/handlers/handlerRemoveProfile.ts ***!
  \***************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerProfileRemove: () => (/* binding */ handlerProfileRemove)\n/* harmony export */ });\n/* harmony import */ var _coockieSessionId__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../coockieSessionId */ \"./src/scripts/services/coockieSessionId.ts\");\n/* harmony import */ var _fetches__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../fetches */ \"./src/scripts/services/fetches.ts\");\n\n\nlet env_ = \"localhost\";\nconst HOST = env_ ? env_ : '';\nenv_ = \"5000\";\nconst PORT = env_ ? env_ : '';\nenv_ = \"http\";\nconst PROTOCOL = env_ ? env_ : '';\nasync function handlerProfileRemove(e) {\n  // Page for a repeat link for authentication.\n  if (e.type && e.type.includes(\"submit\") && e.target.id.includes(\"removing\")) {\n    e.preventDefault();\n\n    // Check cookie name\n    let response = (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.checkCookieExists)(\"userToken\");\n    // true or false\n    if (!response) {\n      console.warn(\"[handlerAddReferral]: 'userToken' not founded in Cookie!\");\n      return false;\n    }\n    // Length of userToken's value.\n    response = (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.getCookie)(\"userToken\");\n    if (response.length === 0) {\n      console.error(\"[handlerAddReferral]: 'userToken'  length is 0/zero !\");\n      return false;\n    }\n    const body_ = JSON.stringify({\n      userToken: response.slice(0)\n    });\n    (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.deleteCookie)(\"userToken\");\n    response = await (0,_fetches__WEBPACK_IMPORTED_MODULE_1__.add)(body_, \"/api/v1/remove\");\n    const href = `${PROTOCOL}://${HOST}:${PORT}/`;\n    location.href = href;\n    return true;\n  }\n  return false;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/handlers/handlerRemoveProfile.ts?");

/***/ }),

/***/ "./src/scripts/services/handlers/handlerTokenRepeats.ts":
/*!**************************************************************!*\
  !*** ./src/scripts/services/handlers/handlerTokenRepeats.ts ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerTokenRepeat: () => (/* binding */ handlerTokenRepeat)\n/* harmony export */ });\nlet env_ = \"localhost\";\nconst HOST = env_ ? env_ : '';\nenv_ = \"5000\";\nconst PORT = env_ ? env_ : '';\nenv_ = \"http\";\nconst PROTOCOL = env_ ? env_ : '';\nasync function handlerTokenRepeat(e) {\n  // Page for a repeat link for authentication.\n  if (e.type && e.type.includes(\"click\") && e.target.type && e.target.type.includes(\"submit\") && e.target.id.includes(\"submit-repeat\")) {\n    e.preventDefault();\n    location.href = `${PROTOCOL}://${HOST}:${PORT}/repeat_token`;\n    return true;\n  }\n  return false;\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/handlers/handlerTokenRepeats.ts?");

/***/ }),

/***/ "./src/scripts/services/handlers/subFunctions.ts":
/*!*******************************************************!*\
  !*** ./src/scripts/services/handlers/subFunctions.ts ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   getUserTokenFromProfilePage: () => (/* binding */ getUserTokenFromProfilePage),\n/* harmony export */   timeOut: () => (/* binding */ timeOut)\n/* harmony export */ });\n/* harmony import */ var _coockieSessionId__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../coockieSessionId */ \"./src/scripts/services/coockieSessionId.ts\");\n/* harmony import */ var _handlerReferralsRemove__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./handlerReferralsRemove */ \"./src/scripts/services/handlers/handlerReferralsRemove.ts\");\n/**\n * This  file has the subfunction for perant functins.\n * This functions is:\n * - 'handlerLoderPage';\n * - 'handlerReferralRemovet'.\n */\n\n\nfunction getUserTokenFromProfilePage(specificUrl) {\n  /**\n   * Here , we receive the 'userToken' from the Cookie.\n   * @returns boolean | string | object\n   */\n  if (window.location.search.length > 2) {\n    return false;\n  }\n\n  // start to work\n  if (window.location.pathname === specificUrl || window.location.pathname.length === specificUrl.length) {\n    // Check cookie name\n    let response = (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.checkCookieExists)(\"userToken\");\n    // true or false\n    if (!response) {\n      console.warn(\"[handlerAddReferral]: 'userToken' not founded in Cookie!\");\n      return false;\n    }\n\n    // Length of userToken's value.\n    response = (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.getCookie)(\"userToken\");\n    return response;\n  }\n  return false;\n}\n\n// param ind this is index from the setInterval\nlet ind = 0;\nlet timeBlockLi;\n/**\n   * This is sub-functin from a page 'listeners'. \\\n   * Block '.reff-view', we can see only if user has a referral code in db. \\\n   * Loading '.reff-view' is hapenning through a timeout if user's referral code was found. \\\n   * That is why 'timOut' working through a setinterval and with 'Index'.\n   * @param index: Number; This is a sessions quantity for the dunction timOut();\n   * @returns void.\n   */\nfunction timeOut(index) {\n  timeBlockLi = setInterval(() => {\n    const liRemovetHTML = document.querySelector(\".reff-view\");\n    if (liRemovetHTML === null && ind <= index) {\n      console.warn(\"[listener] Form was not found the profile removing!\");\n      timeOut(ind);\n      ind += 1;\n      return false;\n    }\n    clearInterval(timeBlockLi);\n    liRemovetHTML.removeEventListener(\"mousedown\", _handlerReferralsRemove__WEBPACK_IMPORTED_MODULE_1__.handlerReferralRemovet);\n    liRemovetHTML.addEventListener(\"mousedown\", _handlerReferralsRemove__WEBPACK_IMPORTED_MODULE_1__.handlerReferralRemovet);\n    ind = 0;\n  }, 700);\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/handlers/subFunctions.ts?");

/***/ }),

/***/ "./src/scripts/services/tokens.ts":
/*!****************************************!*\
  !*** ./src/scripts/services/tokens.ts ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   getUserToken: () => (/* binding */ getUserToken),\n/* harmony export */   setUserToken: () => (/* binding */ setUserToken)\n/* harmony export */ });\n/* harmony import */ var _coockieSessionId__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./coockieSessionId */ \"./src/scripts/services/coockieSessionId.ts\");\n/* harmony import */ var _fetches__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./fetches */ \"./src/scripts/services/fetches.ts\");\nfunction ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }\nfunction _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }\nfunction _defineProperty(e, r, t) { return (r = _toPropertyKey(r)) in e ? Object.defineProperty(e, r, { value: t, enumerable: !0, configurable: !0, writable: !0 }) : e[r] = t, e; }\nfunction _toPropertyKey(t) { var i = _toPrimitive(t, \"string\"); return \"symbol\" == typeof i ? i : i + \"\"; }\nfunction _toPrimitive(t, r) { if (\"object\" != typeof t || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || \"default\"); if (\"object\" != typeof i) return i; throw new TypeError(\"@@toPrimitive must return a primitive value.\"); } return (\"string\" === r ? String : Number)(t); }\n\n\nasync function getUserToken(number) {\n  /**\n   * return JSON '{\"user_token\": < user_token >}' fron servr's response\n   * @param number: string\n   */\n  const body_ = JSON.stringify({\n    userId: String(number)\n  });\n  // Below, GET + POST requsets\n  const responce = await (0,_fetches__WEBPACK_IMPORTED_MODULE_1__.add)(body_, `/api/v1/token/get`);\n  return responce;\n}\nasync function setUserToken(props) {\n  /**\n   *  Saving data in cookie\n   * @param 'user_token': string. This is a key's name of variable from backend. After,\n   * to us need to keep in a Cookie.\n  *\n   *\n   */\n  const {\n    user_token\n  } = _objectSpread({}, props);\n  (0,_coockieSessionId__WEBPACK_IMPORTED_MODULE_0__.setCookie)(\"userToken\", user_token);\n}\n\n//# sourceURL=webpack://frontend-Flask-account/./src/scripts/services/tokens.ts?");

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