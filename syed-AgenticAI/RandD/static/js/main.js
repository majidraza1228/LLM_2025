document.addEventListener('DOMContentLoaded', () => {
    // Handle todo item checkbox toggles
    document.querySelectorAll('.todo-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', async (e) => {
            const todoItem = e.target.closest('.todo-item');
            const todoId = todoItem.dataset.id;

            try {
                const response = await fetch(`/toggle_todo/${todoId}`, {
                    method: 'POST'
                });
                
                if (response.ok) {
                    const data = await response.json();
                    todoItem.classList.toggle('completed');
                }
            } catch (error) {
                console.error('Error toggling todo:', error);
            }
        });
    });

    // Handle todo item deletion
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', async (e) => {
            const todoItem = e.target.closest('.todo-item');
            const todoId = todoItem.dataset.id;

            try {
                const response = await fetch(`/delete_todo/${todoId}`, {
                    method: 'POST'
                });
                
                if (response.ok) {
                    todoItem.remove();
                }
            } catch (error) {
                console.error('Error deleting todo:', error);
            }
        });
    });

    // Add animation to new todos
    document.querySelector('.todo-form').addEventListener('submit', () => {
        setTimeout(() => {
            const newTodo = document.querySelector('.todo-item:first-child');
            if (newTodo) {
                newTodo.style.animation = 'slideIn 0.3s ease';
            }
        }, 100);
    });
}); 