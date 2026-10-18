import { useState } from "react";
import api from "../api";

export default function Upload() {
	const [text, setText] = useState("");
	const [message, setMessage] = useState("");
	const [loading, setLoading] = useState(false);

	const upload = async () => {
		if (!text.trim()) return;

		setLoading(true);
		setMessage("");
		try {
			const res = await api.post("/upload", { text });
			setMessage("Indexed " + res.data.chunks + " chunks");
			setText("");
		} catch {
			setMessage("Upload failed. Is the backend running?");
		} finally {
			setLoading(false);
		}
	};

	return (
		<div className="card">
			<h2>Upload</h2>
			<textarea
				rows="8"
				value={text}
				onChange={e => setText(e.target.value)}
				placeholder="Paste text to index..."
			/>
			<button onClick={upload} disabled={loading || !text.trim()}>
				{loading ? "Indexing..." : "Upload"}
			</button>
			<p>{message}</p>
		</div>
	);
}
