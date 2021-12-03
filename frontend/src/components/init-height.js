/* eslint-disable */

class InitScreenH {

    /**
     * 构造函数
     */
    constructor() {
        this.clasName = 'InitScreenH';
    }

    get getClassName() {
        return this.clasName;
    }

    set setClassName(name) {
        this.clasName = name;
    }

    static install(Vue, options) {
        Vue.directive('init-screen-h', {
            bind(el, binding, vnode, oldVnode) {
                //偏差高度，比如header的高度
                let offsetH;
                offsetH = binding.value ? binding.value : 0;
                //计算并设置el的高度
                el.style.minHeight = window.innerHeight - offsetH + 'px';
            }
        });
    }

}

export default InitScreenH;