/* eslint-disable */
/*
 * 如果需要修改为正常上线模式，请注释下面mock的import代码
 * */
// import "../../config/index"
//import axios from 'axios'
const axios = require('axios');
import API from "./API";

// 请在下方实现自己的后端通信函数
export function post(params) {
    return new Promise((resolve, reject) => {
        let url = API.GET_ESSAYLIST.path
        axios.post(url, params)
            .then(response => {
                resolve(response.data)
            })
            .catch(error => {
                reject(error)
            })
    });
}

export function get(url, params) {
    return new Promise((resolve, reject) => {
        axios.get(url, params)
            .then(response => {
                resolve(response)
            })
            .catch(error => {
                console.log("what happen")
                reject(error)
            })
    });
}