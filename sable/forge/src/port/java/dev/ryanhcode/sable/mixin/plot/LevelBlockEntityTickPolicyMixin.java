package dev.ryanhcode.sable.mixin.plot;

import dev.ryanhcode.sable.sublevel.plot.PlotBlockActivityPolicy;
import com.llamalad7.mixinextras.injector.wrapoperation.Operation;
import com.llamalad7.mixinextras.injector.wrapoperation.WrapOperation;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.Level;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;

/**
 * Adapts Sable's plot ticking responsibility to the Minecraft 1.20.1 call graph.
 *
 * <p>In 1.20.1, overriding {@link ServerLevel#shouldTickBlocksAt(long)} also admits
 * the plot chunk into {@code ServerChunkCache.tickChunks()}, including random/weather
 * ticks whose biome queries cross into deliberately unallocated adjacent plot chunks.
 * Only the gate used while iterating registered block-entity tickers is widened here.
 * This keeps Create and other modded block entities alive without treating the remote
 * storage plot as a naturally ticking overworld chunk.</p>
 */
@Mixin(Level.class)
public abstract class LevelBlockEntityTickPolicyMixin {

    @WrapOperation(
            method = "tickBlockEntities",
            at = @At(
                    value = "INVOKE",
                    target = "Lnet/minecraft/world/level/Level;shouldTickBlocksAt(Lnet/minecraft/core/BlockPos;)Z"
            )
    )
    private boolean sable$shouldTickPlotBlockEntity(final Level instance, final BlockPos pos, final Operation<Boolean> original) {
        return PlotBlockActivityPolicy.shouldProcess(instance, pos, original.call(instance, pos));
    }
}
