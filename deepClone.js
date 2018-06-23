function deepClone(obj) {
    if (!obj) { return obj; } // Handles null values
    if (obj instanceof Date) { return new Date(obj); }
    let primArr = [Boolean,Number,String];
    let res;
    /* if key in object contains an instance of 'new Primitive(example)' the
    cloned object will erroneously be delivered with an empty object for 
    the value, we need to check for this at the top to not let it enter
    the recursive loop when typeof key == object */

    primArr.forEach((prim) => {
        if (obj instanceof prim) {
            res = prim(obj);
        }
    });

    if (typeof res == "undefined") {
        /* Object.prototype.toString() overwritten in custom object
        and when called shows [object Array] instead of [object type] */
        if (Object.prototype.toString.call(obj) === "[object Array]") {
            res = [];
            obj.forEach((v, i) => {
                res[i] = deepClone(v);
            });
        } else if (typeof obj == "object") {
            if (typeof obj.cloneNode == "function") {
                //true so the children of the node will also be cloned
                res = obj.cloneNode(true);    
            } else if (!obj.prototype) {
                    res = {};
                    for (var i in obj) {
                        //begin recursion on nested objects
                        res[i] = deepClone(obj[i]);
                    }
                }
            } else {
                    res = obj;
            }
        } else {
            res = obj;
        }

    return res;
}

module.exports = deepClone