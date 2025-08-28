import React, { useEffect, useState } from 'react';

const ItemsList = () => {
    const [items, setItems] = useState([]);
    const [page, setPage] = useState(1);
    const [pages, setPages] = useState(1);

    useEffect(() => {
        fetch(`/api/items?page=${page}&limit=20`)
            .then(res => res.json())
            .then(data => {
                setItems(data.items);
                setPages(data.pages);
            });
    }, [page]);

    return (
        <div>
            <ul>
                {items.map(item => (
                    <li key={item._id}>{item.name}</li>
                ))}
            </ul>
            <div>
                <button disabled={page === 1} onClick={() => setPage(page - 1)}>Назад</button>
                <span>Страница {page} из {pages}</span>
                <button disabled={page === pages} onClick={() => setPage(page + 1)}>Вперёд</button>
            </div>
        </div>
    );
};

export default ItemsList;