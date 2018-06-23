let assert = require('chai').assert
let should = require('chai').should()
let DeepClone = require('./deepClone')
describe('deepClone', function() {

  it('should clone a basic object', function(){
    let object1, object2;

    object1 = {
      name: 'Alan',
      age: 26
    }

    object2 = DeepClone(object1);

    object1 = JSON.stringify(object1);
    object2 = JSON.stringify(object2);

    object1.should.equal(object2);
  })

  it('should clone an object and maintain its methods', function(){
    let object1, object2;

    object1 = {
      name: 'Alan',
      age: 26,
      method: () => {
        return 2 + 3;
      },
    }

    object2 = DeepClone(object1);

    object1 = JSON.stringify(object1);
    object2 = JSON.stringify(object2);

    object1.should.equal(object2);
  })

  it('should handle null case', function(){
    let object1, object2;

    object1 = {
      name: false,
      age: null,
      and: undefined
    }

    object2 = DeepClone(object1);

    object1 = JSON.stringify(object1);
    object2 = JSON.stringify(object2);

    object1.should.equal(object2);
  })

  it('should handle date object', function(){
    let object1, object2;

    object1 = {
      name: 'Alan',
      age: 26,
      method: () => {
        return 2 + 3;
      },
      time: new Date()
    }

    object2 = DeepClone(object1);

    object1 = JSON.stringify(object1);
    object2 = JSON.stringify(object2);

    object1.should.equal(object2);
  })

  it('should handle primitives declared with \'new\' operator', function(){
    let object1, object2;

    object1 = {
      name: 'Alan',
      age: 26,
      method: () => {
        return 2 + 3;
      },
      time: new Date(),
      string: new String('Dublin')
    }

    object2 = DeepClone(object1);

    object1 = JSON.stringify(object1);
    object2 = JSON.stringify(object2);

    object1.should.equal(object2);
  })



});