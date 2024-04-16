// Very different problem than I expected and very broad, no help from the interviewer on what exactly to implement - Position: Senior SDE Google Cloud:

// You have a backend system that stores all versions of a JSON object. You need to reduce the amount of data stored, how would you design the API.
// I assumed they wanted to write a function to do a JSON diff of current state vs new state so we only store the diff. Had no feedback whatsoever from the interviewer while working on it, so I have no idea what they expected.

// Ended up creating a function that returns a diff give two json objects and that's all I managed to do with the time I had. Still waiting to hear back if its a pass or not.


/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */
function objDiff(obj1, obj2) {
    if(obj1 === obj2){return {}; }
    if(obj1 === null || obj2 === null){
        return [obj1 , obj2];
    }

    if(typeof obj1 !== 'object' || typeof obj2 !== 'object'){
        return [obj1 , obj2];
    }

    if(Array.isArray(obj1) !== Array.isArray(obj2)){
        return [obj1 ,obj2];
    }


    const retObj = {};
    for(const key in obj1){
        if(key in obj2){
            const diff = objDiff(obj1[key] , obj2[key]);
            if(Object.keys(diff).length>0){
                retObj[key] = diff;
            }
        }
    }

    return retObj;

};