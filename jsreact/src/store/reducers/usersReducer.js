const initState = {

    users: []
}

export const usersReducer = (state = initState, action) => {

    if (action.type === "addUser") {

        return {
            ...state,
            users: [...state.users, {name: action.name, password: action.password}]
        }         
    } 
    
    else {
        
        return {
            ...state
        }      
    }
}