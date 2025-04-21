const socket = io();

function joinAuction(auctionId) {
    socket.emit('join_auction', { auction_id: auctionId });

    socket.on('new_bid', (bid) => {
        updateBidDisplay(bid);
    });
}

function placeBid(auctionId, amount) {
    socket.emit('place_bid', {
        auction_id: auctionId,
        amount: amount
    });
}