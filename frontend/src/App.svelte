<script>
  import axios from 'axios';
  import { onMount } from 'svelte';

  const API_URL = import.meta.env.VITE_API_URL;

  let task = '';
  let tasks = [];
  let editId = null;

  // FETCH TASKS
  async function fetchTasks() {             //get task from backend

    try {

      const response = await axios.get(`${API_URL}/tasks`); //calls GET/tasks

      tasks = response.data;

    } catch (error) {

      console.error('Fetch Error:', error);

    }
  }

  // ADD TASK
  async function addTask() {

    if (!task.trim()) return;

    try {

      await axios.post(`${API_URL}/tasks`, {         //calls POST/tasks
        title: task
      });

      task = '';

      await fetchTasks();

    } catch (error) {

      console.error('Add Error:', error);

    }
  }

  // SELECT TASK
  function editTask(item) {

    task = item.title;

    editId = item.id;

    console.log('Editing Task:', editId);
  }

  // UPDATE TASK
  async function updateTask() {

    if (!task.trim()) return;

    try {

      console.log('Updating Task:', editId);

      const response = await axios.put(    //calls PUT/tasks/id
        `${API_URL}/tasks/${editId}`,
        {
          title: task
        }
      );

      console.log(response.data);

      task = '';

      editId = null;

      await fetchTasks();

    } catch (error) {

      console.error('Update Error:', error);

    }
  }

  // DELETE TASK
  async function deleteTask(id) {

    try {

      await axios.delete(`${API_URL}/tasks/${id}`);

      await fetchTasks();

    } catch (error) {

      console.error('Delete Error:', error);

    }
  }

  // LOAD TASKS
  onMount(() => {

    fetchTasks();

  });
</script>

<div class="container">

  <div class="card">

    <h1>Smart Task App</h1>

    <div class="input-group">

      <input
        bind:value={task}
        placeholder="Enter task..."
      />

      {#if editId === null}

        <button on:click={addTask}>
          Add Task
        </button>

      {:else}

        <button
          class="update-btn"
          on:click={updateTask}>
          Update
        </button>

      {/if}

    </div>

    {#if tasks.length === 0}

      <p class="empty">
        No tasks available
      </p>

    {/if}

    <div class="tasks">

      {#each tasks as item}

        <div class="task-item">

          <span>{item.title}</span>

          <div class="actions">

            <button
              class="edit-btn"
              on:click={() => editTask(item)}
            >
              Edit
            </button>

            <button
              class="delete-btn"
              on:click={() => deleteTask(item.id)}
            >
              Delete
            </button>

          </div>

        </div>

      {/each}

    </div>

  </div>

</div>

<style>

  body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f5f7fb;
  }

  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }

  .card {
    width: 700px;
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
  }

  h1 {
    text-align: center;
    margin-bottom: 30px;
  }

  .input-group {
    display: flex;
    gap: 10px;
  }

  input {
    flex: 1;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ddd;
    font-size: 16px;
  }

  button {
    padding: 15px 20px;
    border: none;
    border-radius: 10px;
    background: #4f46e5;
    color: white;
    cursor: pointer;
    font-size: 14px;
  }

  .tasks {
    margin-top: 30px;
  }

  .task-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #fafafa;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
    border: 1px solid #eee;
  }

  .actions {
    display: flex;
    gap: 10px;
  }

  .edit-btn {
    background: #10b981;
  }

  .update-btn {
    background: #f59e0b;
  }

  .delete-btn {
    background: #ef4444;
  }

  .empty {
    text-align: center;
    color: gray;
    margin-top: 20px;
  }

</style>