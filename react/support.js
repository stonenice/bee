import {fromJS,is} from 'immutable'

export const sleep=(ms=1000)=>{
    return new Promise(resolve => setTimeout(resolve, ms))
}

export const applyReducer=(...args)=>{
    if(!args||args.length<=0){
        throw Error('no reducers, so it cannot be applied.');
    }
     let cr={};
    for(let arg of args){
        let initialState=fromJS(arg.initialState);
        cr[arg.namespace]=(state=initialState, action)=>{
            let funcs=arg.reducers;
            if(funcs){
                let s=state.get(arg.namespace);
                let nextState=fromJS(s?s:state);
                for(let k in funcs){
                    nextState=fromJS(funcs[k](nextState.toJS(),action));
                }
                return nextState;
            }else{
                return state;
            }
        }
    }
    
    return cr;
}
