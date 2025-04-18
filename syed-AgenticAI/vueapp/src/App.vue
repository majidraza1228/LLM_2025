<template>
  <div id="app">
    <h1>User Management</h1>
    <form @submit.prevent="addUser">
      <input v-model="newUser" placeholder="Enter user name" />
      <button type="submit">Add User</button>
    </form>
    <ul>
      <li v-for="(user, index) in users" :key="index">
        {{ user }}
        <button @click="removeUser(index)">Remove</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newUser: '',
      users: []
    };
  },
  methods: {
    addUser() {
      if (this.newUser.trim() !== '') {
        this.users.push(this.newUser.trim());
        this.newUser = '';
      }
    },
    removeUser(index) {
      this.users.splice(index, 1);
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 50px;
}
form {
  margin-bottom: 20px;
}
input {
  padding: 5px;
  font-size: 16px;
}
button {
  margin-left: 10px;
  padding: 5px 10px;
  font-size: 16px;
  cursor: pointer;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 5px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
