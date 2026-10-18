import axios from "axios";

// Set REACT_APP_API_URL to point at a different backend.
export default axios.create({
	baseURL: process.env.REACT_APP_API_URL || "http://localhost:8000",
});
