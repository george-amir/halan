function compose(f,g){
    return function(x){
        return f(g(x))
    }
}
h = compose(function(arg){return arg**2}, function(arg){return arg+1})
console.log(h(6))