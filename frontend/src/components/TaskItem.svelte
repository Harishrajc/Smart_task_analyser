<script>
  export let task;
  export let onDelete;
</script>

<div class="task-item">
  <span>{task}</span>

  <button class="delete-btn" on:click={onDelete}>
    Delete
  </button>
</div>