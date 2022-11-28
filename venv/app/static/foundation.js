//Idea of deletion is inspired from "Tech with Tim" Youtube channel: https://www.youtube.com/watch?v=dam0GPOAvVI

// JS function to delete a workoutlog
function deleteTodo(todoId) {
    fetch("/delete-todo", { method: "POST", body: JSON.stringify({ todoId: todoId }),
    }).then((_res) => {
        window.location.href = "/plan";
    });
}
// JS function to delete a specific measurelog
function deleteMeasureLog(measurelogId) {
    fetch("/deletemeasurelog", { method: "POST", body: JSON.stringify({ measurelogId: measurelogId }), weight: JSON.stringify({ measurelogId: measurelogId }),
    }).then((_res) => {
        window.location.href = "/userProfile";
    });
}

