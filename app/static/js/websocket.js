const socket = io();

function joinAuctionRoom(auctionId) {
    socket.emit('join_auction', { auction_id: auctionId });
}

socket.on('new_bid', (data) => {
    console.log('New bid received:', data);
});