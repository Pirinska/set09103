

function deleteMeasureLog(measurelogId) {
    fetch("/deletemeasurelog", { method: "POST", calf: JSON.stringify({ measurelogId: measurelogId }),
    }).then((_res) => {
        window.location.href = "/userProfile";
    });
}

function deleteTodo(todoId) {
    fetch("/delete-todo", { method: "POST", body: JSON.stringify({ todoId: todoId }),
    }).then((_res) => {
        window.location.href = "/plan";
    });
}