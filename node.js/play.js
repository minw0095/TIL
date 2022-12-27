const person = {
    name:'dd',
    age: 10,
    // greet: () =>{
    //     console.log('Hi,' + this.name);
    // }
    greet() {
        console.log('Hi' + this.name)
    }
};


const hobbies = ['11','22'];

console.log(hobbies.map(hobby => {
    return 'hooby: ' + hobby;
}));
console.log(hobbies)