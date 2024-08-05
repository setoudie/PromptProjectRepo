// export const PromptList = [
//   {
//     "content": "new test",
//     "id": 13,
//     "note": 0,
//     "owner": "user1",
//     "price": 1000,
//     "status": "active"
//   },
//   {
//     "content": "tesd post",
//     "id": 6,
//     "note": 6,
//     "owner": "poss",
//     "price": 4200,
//     "status": "active"
//   },
//   {
//     "content": "ceci est un test",
//     "id": 1,
//     "note": 6,
//     "owner": "user1",
//     "price": 1000,
//     "status": "active"
//   },
//   {
//     "content": "tester",
//     "id": 12,
//     "note": 2,
//     "owner": "user11",
//     "price": 5800,
//     "status": "active"
//   },
//   {
//     "content": "postmaest",
//     "id": 8,
//     "note": 0,
//     "owner": "user1",
//     "price": 1800,
//     "status": "active"
//   },
//   {
//     "content": "odc",
//     "id": 16,
//     "note": 0,
//     "owner": "sek",
//     "price": 3400,
//     "status": "active"
//   },
//   {
//     "content": "new user1 ",
//     "id": 15,
//     "note": -1,
//     "owner": "user1",
//     "price": 3800,
//     "status": "active"
//   },
//   {
//     "content": "prompt to delete",
//     "id": 10,
//     "note": 0,
//     "owner": "user2",
//     "price": 1000,
//     "status": "review"
//   },
//   {
//     "content": "new test",
//     "id": 14,
//     "note": 0,
//     "owner": "user1",
//     "price": 1000,
//     "status": "review"
//   },
//   {
//     "content": "prompt test",
//     "id": 11,
//     "note": 2,
//     "owner": "user11",
//     "price": 5800,
//     "status": "active"
//   },
//   {
//     "content": "prompt to delete",
//     "id": 9,
//     "note": 3,
//     "owner": "user2",
//     "price": 1000,
//     "status": "review"
//   },
//   {
//     "content": "postmat test",
//     "id": 7,
//     "note": 4,
//     "owner": "user1",
//     "price": 1000,
//     "status": "review"
//   }
// ]

const url = 'http://127.0.0.1:5000/prompts/dashboard';
let PromptList = [];

fetch(url)
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.length; i++) {
      PromptList.push(data[i])
    }
    console.log(PromptList);
    // alert()
    // return PromptList
  })
  .catch(error => console.error('Erreur :', error));

export default PromptList;
