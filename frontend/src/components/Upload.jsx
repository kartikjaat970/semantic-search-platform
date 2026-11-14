import { useEffect, useState } from "react";
import api from "../api";

export default function Upload({ onClose }) {
	const [text, setText] = useState("");
	const [message, setMessage] = useState("");
	const [uploaded, setUploaded] = useState(false);
	const [loading, setLoading] = useState(false);

	// Close the pop-up with the Escape key
	useEffect(() => {
		const onKey = e => e.key === "Escape" && onClose();
		window.addEventListener("keydown", onKey);
		return () => window.removeEventListener("keydown", onKey);
	}, [onClose]);

	const upload = async () => {
		if (!text.trim()) return;

		setLoading(true);
		setMessage("");
		setUploaded(false);
		try {
			const res = await api.post("/upload", { text });
			setMessage("Indexed " + res.data.chunks + " chunks");
			setUploaded(true);
			setText("");
		} catch {
			setMessage("Upload failed. Is the backend running?");
		} finally {
			setLoading(false);
		}
	};

	return (
		<div className="overlay" onClick={onClose}>
			<div className="modal" onClick={e => e.stopPropagation()}>
				<button className="close" onClick={onClose} aria-label="Close">
					&times;
				</button>
				<h2>Upload</h2>
				<p className="hint">Paste text to add it to your search index.</p>
				<textarea
					rows="8"
					value={text}
					onChange={e => setText(e.target.value)}
					placeholder="Paste text to index..."
				/>
				<div className="actions">
					<button onClick={upload} disabled={loading || !text.trim()}>
						{loading ? "Indexing..." : "Upload"}
					</button>
					<button className="ghost" onClick={onClose}>
						{uploaded ? "Go to search" : "Skip to search"}
					</button>
				</div>
				{message && <p className={uploaded ? "success" : "error"}>{message}</p>}
			</div>
		</div>
	);
}
