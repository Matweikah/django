app.get('/api/items', async (req, res) => {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 20;
    const skip = (page - 1) * limit;

    // Получить общее количество
    const total = await Item.countDocuments();

    // Получить только нужную часть
    const items = await Item.find().skip(skip).limit(limit);

    res.json({
        items,
        total,
        page,
        pages: Math.ceil(total / limit)
    });
});