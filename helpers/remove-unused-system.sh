#!/bin/bash
#
# Remove unused files, or files that should not be used

if [ -z "$TREE_SPARSE" ]; then
    echo "TREE_SPARSE is unset!"
    exit 1
fi

source "droid-system-device/helpers/remove-unused-$TREE.sh"

rm -rf "$TREE_SPARSE"/apex/com.android.adbd.capex
rm -rf "$TREE_SPARSE"/apex/com.android.adservices.capex
rm -rf "$TREE_SPARSE"/apex/com.android.appsearch.apex
rm -rf "$TREE_SPARSE"/apex/com.android.art.capex
rm -rf "$TREE_SPARSE"/apex/com.android.btservices.apex
rm -rf "$TREE_SPARSE"/apex/com.android.cellbroadcast.capex
rm -rf "$TREE_SPARSE"/apex/com.android.extservices.capex
rm -rf "$TREE_SPARSE"/apex/com.android.ipsec.capex
rm -rf "$TREE_SPARSE"/apex/com.android.mediaprovider.capex
rm -rf "$TREE_SPARSE"/apex/com.android.neuralnetworks.capex
rm -rf "$TREE_SPARSE"/apex/com.android.ondevicepersonalization.apex
rm -rf "$TREE_SPARSE"/apex/com.android.permission.capex
rm -rf "$TREE_SPARSE"/apex/com.android.scheduling.apex
rm -rf "$TREE_SPARSE"/apex/com.android.sdkext.apex
rm -rf "$TREE_SPARSE"/apex/com.android.tethering.capex
rm -rf "$TREE_SPARSE"/apex/com.android.uwb.apex
rm -rf "$TREE_SPARSE"/apex/com.android.wifi.capex

rm -rf "$TREE_SPARSE"/bin/hw/android.hardware.neuralnetworks@1.3-service-armnn-gpu
rm -rf "$TREE_SPARSE"/bin/surfaceflinger
rm -rf "$TREE_SPARSE"/bin/update_engine

rm -rf "$TREE_SPARSE"/etc/models

rm -rf "$TREE_SPARSE"/lib/libGLES_mali.so
rm -rf "$TREE_SPARSE"/lib/libsprdfaceid.so

rm -rf "$TREE_SPARSE"/lib/libSprdAppImageFilter.so
rm -rf "$TREE_SPARSE"/lib64/libSprdAppImageFilter.so
rm -rf "$TREE_SPARSE"/lib/libSprdImageFilterResource.so
rm -rf "$TREE_SPARSE"/lib64/libSprdImageFilterResource.so
rm -rf "$TREE_SPARSE"/lib/libpdfium.so
rm -rf "$TREE_SPARSE"/lib64/libpdfium.so
rm -rf "$TREE_SPARSE"/lib/libhwui.so
rm -rf "$TREE_SPARSE"/lib64/libhwui.so

rm -rf "$TREE_SPARSE"/lib64/libaiactiver.so
rm -rf "$TREE_SPARSE"/lib64/libaiactiver_core.so
rm -rf "$TREE_SPARSE"/lib64/libfaceverify.so
rm -rf "$TREE_SPARSE"/lib64/libinfo.so
rm -rf "$TREE_SPARSE"/lib64/libsprdfarcnn_SDK.so
