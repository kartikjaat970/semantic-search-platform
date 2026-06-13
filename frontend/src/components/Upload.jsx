import { useState } from "react";
import api from "../api";

export default function Upload() {
	const [text, setText] = useState("");
	const [message, setMessage] = useState("");

	const upload = async () => {
		try {
			const res = await api.post("/upload", { text });
			setMessage("Indexed " + res.data.chunks + " chunks");
		} catch {
			setMessage("Upload failed");
		}
	};

	return (
		<div className="card">
			<h2>Upload</h2>
			<textarea
				rows="8"
				value={text}
				onChange={e => setText(e.target.value)}
			/>
			<button onClick={upload}>Upload</button>
			<p>{message}</p>
		</div>
	);
}