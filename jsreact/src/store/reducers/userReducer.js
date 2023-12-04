const initState = {
    
    user: {
        name: null,
        password: null
    }
}

export const userReducer = (state = initState, action) => {

    if (action.type === "add") {

        return {
            ...state,
            user: {
                name: action.name,
                password: action.password
            }
        }
    } 

    else if (action.type === "delete") {

        return {
            ...state,
            user: {
                name: null,
                password: null
            }
        }
    } 
    
    else {

        return {
            ...state
        }
    }
}