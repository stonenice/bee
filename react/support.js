import {fromJS,is} from 'immutable'

//support to combine a extension reducer
const applyReducer=(...args)=>{
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
                let oldState=fromJS(s?s:state);
                for(let k in funcs){
                    let newState=fromJS(funcs[k](oldState.toJS(),action));
                    if(!is(oldState,newState)){
                        return oldState.mergeDeep(newState);
                    }
                }
                return state;
            }else{
                return state;
            }
        }
    }
    
    return cr;
}
