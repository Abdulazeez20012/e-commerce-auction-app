const socket = io('http://localhost:5000');

socket.on('new_bid', (data) => {
    const auctionElement = document.querySelector(`.auction[data-id="${data.auction_id}"]`);
    if (auctionElement) {
        auctionElement.querySelector('.current-price').textContent = `$${data.amount}`;
    }
});

function joinAuctionRoom(auctionId) {
    socket.emit('join_auction', { auction_id: auctionId });
}