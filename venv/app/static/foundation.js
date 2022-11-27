function deleteTodo(todoId) {
    fetch("/delete-todo", { method: "POST", body: JSON.stringify({ todoId: todoId }),
    }).then((_res) => {
        window.location.href = "/plan";
    });
}

function deleteMeasureLog(measurelogId) {
    fetch("/deletemeasurelog", { method: "POST", body: JSON.stringify({ measurelogId: measurelogId }), weight: JSON.stringify({ measurelogId: measurelogId }),
    }).then((_res) => {
        window.location.href = "/userProfile";
    });
}