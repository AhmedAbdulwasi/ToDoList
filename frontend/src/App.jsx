import {useState,useEffect} from "react";
import "./App.css";
import TasksList from "./components/TasksList";
import TasksForm from "./components/TasksForm";

function App() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    fetchTasks()
  }, [])

  const fetchTasks = async () => {
    const response = await fetch("http://127.0.0.1:5000/api/showtasks")
    const data = await response.json()
    setTasks(data.tasks)
  }

  return (
    <>
      <div className="maintitle">
        <h1>Simple ToDoList</h1>
      </div>
      <TasksList tasks={tasks} fetchTasks={fetchTasks} />
      <TasksForm fetchTasks={fetchTasks} />
    </>
  )
}

export default App;